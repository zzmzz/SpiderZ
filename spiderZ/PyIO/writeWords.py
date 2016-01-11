#!/usr/bin/python
# coding=utf-8
import re
import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client.spiderDB
collection = db.spider
collection.remove()

class Write():
    @staticmethod
    def write(url, word_list):
        try:
            for words in word_list:
                collection.insert({"content": words, "url": url})
        except Exception, e:
            print url, word_list, e
