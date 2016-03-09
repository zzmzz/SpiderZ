#!/usr/bin/python
# coding=utf-8
import re
import sys
import urllib2
import chardet
from PyIO.writeWords import Write
from enums import Language
from Utils.logFactory import LogFactory

reload(sys)
sys.setdefaultencoding('utf-8')


class GetWords:
    logger = LogFactory.getlogger("GetWords")

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
        if html is None:
            html = GetWords.__getContent(url)
        try:
            words = GetWords.__getChinese(html)
            Write.write(url, words)
        except Exception, e:
            GetWords.logger.error(url + " " + str(e))

    @staticmethod
    def getEnglish(url, html=None):
        return html

    @staticmethod
    def __getChinese(html):
        raw = html
        codec = chardet.detect(raw)
        try:
            raw = unicode(raw, codec['encoding'], 'ignore')
        except Exception, e:
            GetWords.logger.error(str(e))
            raise Exception, "undefined codec"
        words = re.findall(ur"[\u4e00-\u9fa5]+", raw)
        if words.__len__() == 0:
            raise Exception, "cannot find any words"
        return words

    @staticmethod
    def __getContent(url):
        print url
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        req = urllib2.Request(url=url)
        html = urllib2.urlopen(req).read()
        return html
