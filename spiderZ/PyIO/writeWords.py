#!/usr/bin/python
# coding=utf-8
import pymongo
from WordSplit.splitAdapter import SplitAdapter


class Write():

    @staticmethod
    def clean():
        client = pymongo.MongoClient('mongodb://z:z@localhost:27017/')
        db = client.spiderDB
        collection = db.spider
        collection.remove()
        client.close()

    @staticmethod
    def write(url, word_list):
        client = pymongo.MongoClient('mongodb://z:z@localhost:27017/')
        db = client.spiderDB
        collection = db.spider
        try:
            for words in word_list:
                ws = SplitAdapter.split(words)
                for w in ws:
                    collection.insert({"content": w, "url": url})
        except Exception, e:
            print url, word_list, e
        finally:
            client.close()
