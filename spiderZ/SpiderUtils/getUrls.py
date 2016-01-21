#!/usr/bin/python
# coding=utf-8
from bs4 import BeautifulSoup
import time, re, urllib2
from urlparse import *
from PyMemcached.Locks.bloomFilterLock import BloomFilterLock


class UrlScan:
    @staticmethod
    def scanpage(html, url, isout, pattern=None):
        try:
            BloomFilterLock(url).lock_and_do()
            results = []
            n = 0
            soup = BeautifulSoup(html, "lxml")
            pageurls = []
            Upageurls = {}
            if (pattern != None):
                pageurls = soup.find_all("a", href=re.compile(pattern))
            else:
                pageurls = soup.find_all("a", href=re.compile('http'))
            for link in pageurls:
                u = link.get("href")
                if (BloomFilterLock(u).lock_and_do()):
                    results.append(u)
            return results
        except Exception, e:
            print url
            print e
