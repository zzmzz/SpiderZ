#!/usr/bin/python
# coding=utf-8
from bs4 import BeautifulSoup
from PyMemcached.Locks.bloomFilterLock import BloomFilterLock
from Utils.logFactory import LogFactory
import htmllib, formatter, re

logger = LogFactory.getlogger("UrlScan")


class UrlScan:
    @staticmethod
    def scanpage(html, url, pattern=None):
        try:
            BloomFilterLock(url).lock_and_do()
            results = []
            format = formatter.AbstractFormatter(formatter.NullWriter())
            ptext = htmllib.HTMLParser(format)
            ptext.feed(html)
            for link in ptext.anchorlist:
                if pattern is None:
                    pattern = 'http'
                r = re.findall(pattern, link)
                if r is None or len(r) == 0:
                    continue
                if BloomFilterLock(link).lock_and_do():
                    results.append(link)
            return results
        except Exception, e:
            logger.error("catch urls exception url: " + url + " error: " + str(e))
