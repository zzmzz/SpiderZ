#!/usr/bin/python
# coding=utf-8
import pymongo
from Utils.config import Config

class PyMongoUtil():
    @staticmethod
    def clean():
        client = PyMongoUtil.__get_client()
        collection = PyMongoUtil.__get_data_save_collection(client)
        collection.remove()
        client.close()

    @staticmethod
    def write(url, word_list):
        client = PyMongoUtil.__get_client()
        collection = PyMongoUtil.__get_data_save_collection(client)
        try:
            for w in word_list:
                collection.insert({"content": w, "url": url})
        except Exception, e:
            print url, word_list, e
        finally:
            client.close()

    @staticmethod
    def __get_client():
        ip = Config.getProperty('mongo', 'addr')
        port = int(Config.getProperty('mongo', 'port'))
        client = pymongo.MongoClient(ip, port)
        return client

    @staticmethod
    def __get_data_save_collection(client):
        db = client.get_database(Config.getProperty('mongo','resultdb'))
        cl = db.get_collection(Config.getProperty('mongo','resultcollection'))
        return cl