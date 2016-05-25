# !/usr/bin/python
# coding=utf-8
from ProcessPool.pool import PyPool
from PyIO.pyMongoUtil import PyMongoUtil
from PyMemcached.memcacheUtil import MemcacheUtil
from QueueListener.listener import MyListener
from SpiderUtils.bloomFilter import SpiderBloomFilter
from SpiderUtils.spider import Spider
from SpiderUtils.spiderStrategy import SpiderStrategy
from Statics.wordCount import WordCount
from Utils.logFactory import LogFactory
from SpiderUtils.SpiderMode.regexMode import Regex
from SpiderUtils.enums import Language
from SpiderUtils.getWords import GetWords

logger = LogFactory.getlogger("main")

# clean old data
PyMongoUtil.clean()
MemcacheUtil.clean()

# create bloom filter
SpiderBloomFilter()

# multitask prepare
queue = PyPool.get_queue()
lock = PyPool.get_lock()
listener = MyListener()


def err():
    print("please enter the right select")


while True:
    url = raw_input("Please input url:\n")
    print("checking url...")
    if not url.startswith("http"):
        url = "http://" + url
    try:
        statusCode = GetWords.try_connect(url)
    except Exception, e:
        print(str(e))
        continue
    if statusCode != 200:
        print "cannot connect to the website"
    else:
        break

while True:
    depth = raw_input("Please input depth:\n")
    if not depth.isdigit():
        print("please enter a number\n")
    else:
        break

while True:
    isOut = raw_input("Limit the domain? Y/N\n")
    isOut = str.lower(isOut)
    if isOut != 'y' and isOut != 'n':
        err()
        continue
    else:
        if str.lower(isOut)=='y':
            isOut = False
        else:
            isOut = True
        break

while True:
    md = raw_input("Select the crawler mode:\n1.Chinese 2.English 3.Korean 4.Regex\n")
    if not md.isdigit() or int(md) <= 0 or int(md) >= 5:
        err()
        continue
    else:
        md = int(md)
        if md == 4:
            regex = raw_input("please enter regex string:\n")
            mode = Regex(regex)
        else:
            mode = Language.get_enum(md)
        break

s = SpiderStrategy(url, int(depth), isOut, None, mode)
Spider(s).get_all_words(queue, lock)
listener.listen(lock, queue)
WordCount.calc_count()
