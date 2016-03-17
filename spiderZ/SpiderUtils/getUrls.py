#!/usr/bin/python
# coding=utf-8
from bs4 import BeautifulSoup
import time, re, urllib2
from urlparse import *
from PyMemcached.Locks.bloomFilterLock import BloomFilterLock
from Utils.logFactory import LogFactory

logger = LogFactory.getlogger("UrlScan")


class UrlScan:
    @staticmethod
    def scanpage(html, url, isout, pattern=None):
        try:
            BloomFilterLock(url).lock_and_do()
            results = []
            soup = BeautifulSoup(html, "lxml")
            if pattern is not None:
                pageurls = soup.find_all("a", href=re.compile(pattern))
            else:
                pageurls = soup.find_all("a", href=re.compile('http'))
            for link in pageurls:
                u = link.get("href")
                if BloomFilterLock(u).lock_and_do():
                    results.append(u)
            return results
        except Exception, e:
            logger.error("catch urls exception url: " + url + " error: " + str(e))
