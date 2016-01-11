#!/usr/bin/python
# coding=utf-8
import re
import sys
import urllib2
import chardet
from PyIO.writeWords import Write
from enums import Language

reload(sys)
sys.setdefaultencoding('utf-8')


class GetWords:
    @staticmethod
    def getWords(url, language=Language.All):
        operator = {Language.All: GetWords.getAll, Language.English: GetWords.getEnglish,
                    Language.Chinese: GetWords.getChinese}
        return operator.get(language)(url);

    @staticmethod
    def getAll(url):
        html = GetWords.__getContent(url);
        GetWords.getChinese(url, html)
        GetWords.getEnglish(url, html)
        return html

    @staticmethod
    def getChinese(url, html=None):
        if (html is None):
            html = GetWords.__getContent(url)
        try:
            words = GetWords.__getChinese(html)
            Write.write(url, words)
        except Exception, e:
            print url
            print e

    @staticmethod
    def getEnglish(url, html=None):
        html = ""
        return html

    @staticmethod
    def __getChinese(html):
        codec = chardet.detect(html)
        html = unicode(html, codec['encoding'])
        words = re.findall(ur"[\u4e00-\u9fa5]+", html)
        return words

    @staticmethod
    def __getContent(url):
        print url
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        req = urllib2.Request(url=url, headers=headers)
        html = urllib2.urlopen(req).read()
        return html
