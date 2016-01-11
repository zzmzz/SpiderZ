from SpiderUtils.spider import Spider
from SpiderUtils.spiderStrategy import SpiderStrategy
from SpiderUtils.enums import Language
from Statics.wordCount import WordCount
s=SpiderStrategy("http://www.creditease.com",2,True,None,Language.Chinese)
Spider(s).get_all_words()
WordCount.calc_count()