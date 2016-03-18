#!/usr/bin/python
# coding=utf-8
import re
import sys
import chardet
from Utils.logFactory import LogFactory
import urllib2
import zlib

reload(sys)
sys.setdefaultencoding('utf-8')

logger = LogFactory.getlogger("GetWords")


class GetWords:
    headers = headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36'}

    @staticmethod
    def get_chinese(html):
        raw = GetWords.__get_unicode_content(html)
        words = re.findall(ur"[\u4e00-\u9fa5]+", raw)
        if words.__len__() == 0:
            raise Exception, "cannot find any words"
        return words

    @staticmethod
    def get_english(html):
        s = re.findall("\w+", str.lower(html))
        return s

    @staticmethod
    def get_korean(html):
        raw = GetWords.__get_unicode_content(html)
        words = re.findall(ur"[\uAC00-\uD7AF]+", raw)
        if words.__len__() == 0:
            raise Exception, "cannot find any words"
        return words

    @staticmethod
    def get_by_regex(html, pattern):
        ws = re.findall(pattern, html)
        return ws

    @staticmethod
    def __get_unicode_content(html):
        raw = html
        codec = chardet.detect(raw)
        try:
            code = codec['encoding']
            if code is None:
                code = 'utf-8'
            raw = unicode(raw, code, 'ignore')
        except Exception, e:
            logger.error(str(e))
            raise Exception, "undefined codec"
        return raw

    @staticmethod
    def get_content(url):
        print url
        request = urllib2.Request(url, headers=GetWords.headers)
        request.add_header('Accept-encoding', 'gzip')
        opener = urllib2.build_opener()
        response = opener.open(request)
        html = response.read()
        gzipped = response.headers.get('Content-Encoding')
        if gzipped:
            html = zlib.decompress(html, 16 + zlib.MAX_WBITS)
        return html

    @staticmethod
    def try_connect(url):
        request = urllib2.Request(url, headers=GetWords.headers)
        request.add_header('Accept-encoding', 'gzip')
        opener = urllib2.build_opener()
        response = opener.open(request).getcode()
        return response
