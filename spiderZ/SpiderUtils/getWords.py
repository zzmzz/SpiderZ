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
        html = GetWords.getChinese(url)
        GetWords.getEnglish(url)
        return html

    @staticmethod
    def getChinese(url):
        html = ""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
            req = urllib2.Request(url=url, headers=headers)
            html = urllib2.urlopen(req).read()
            words = GetWords.__getChinese(html)
            print url
            Write.write(url, words)
            # for w in words:
            #   print w.decode("utf-8", "ignore")
        except Exception, e:
            print url
            print e
            pass
        return html

    @staticmethod
    def getEnglish(url):
        html = ""
        return html

    @staticmethod
    def __getChinese(html):
        codec = chardet.detect(html)
        html = unicode(html, codec['encoding'])
        words = re.findall(ur"[\u4e00-\u9fa5]+", html)
        return words
