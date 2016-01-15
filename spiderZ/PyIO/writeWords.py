#!/usr/bin/python
# coding=utf-8
import pymongo
from WordSplit.splitAdapter import SplitAdapter

client = pymongo.MongoClient('localhost', 27017)
db = client.spiderDB
collection = db.spider
collection.remove()


class Write():
    @staticmethod
    def write(url, word_list):
        try:
            for words in word_list:
                ws = SplitAdapter.split(words)
                for w in ws:
                    collection.insert({"content": w, "url": url})
        except Exception, e:
            print url, word_list, e
