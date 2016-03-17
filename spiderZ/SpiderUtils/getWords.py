#!/usr/bin/python
# coding=utf-8
import re
import sys
import urllib2
import chardet
from Utils.logFactory import LogFactory
import zlib

reload(sys)
sys.setdefaultencoding('utf-8')

logger = LogFactory.getlogger("GetWords")


class GetWords:
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
    def get_by_regex(html,pattern):
        ws = re.findall(pattern,html)
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
