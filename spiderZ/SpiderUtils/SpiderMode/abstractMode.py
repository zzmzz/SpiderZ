#!/usr/bin/python
# coding=utf-8
from abc import ABCMeta, abstractmethod
import sys
import urllib2
import zlib
from Utils.logFactory import LogFactory
from PyIO.pyMongoUtil import PyMongoUtil

reload(sys)
sys.setdefaultencoding('utf-8')

logger = LogFactory.getlogger("Mode")


class AbstractMode:
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    def _get_content(self, url):
        print url
        request = urllib2.Request(url)
        request.add_header('Accept-encoding', 'gzip')
        opener = urllib2.build_opener()
        response = opener.open(request)
        html = response.read()
        gzipped = response.headers.get('Content-Encoding')
        if gzipped:
            html = zlib.decompress(html, 16 + zlib.MAX_WBITS)
        return html

    def get_words(self, url):
        html = self._get_content(url)
        try:
            words = self.catch_words(html)
            wlist = []
            for wd in words:
                wlist.extend(self.analyze(wd))
            PyMongoUtil.write(url, wlist)
        except Exception, e:
            logger.error(url + " " + str(e))
        return html

    @abstractmethod
    def catch_words(self, html):
        pass

    @abstractmethod
    def analyze(self, word):
        pass
