#!/usr/bin/python
# coding=utf-8
from bs4 import BeautifulSoup
import time, re, urllib2
from urlparse import *
from bloomFilter import Bloom_Filter


class UrlScan:
    URLPOOL = Bloom_Filter()

    @staticmethod
    def scanpage(html, url, isout, pattern=None):
        try:
            UrlScan.URLPOOL.mark_value(url)
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
                if (UrlScan.URLPOOL.exists(u)):
                    continue
                else:
                    UrlScan.URLPOOL.mark_value(u)
                    results.append(u)
            return results
        except Exception, e:
            print url
            print e
