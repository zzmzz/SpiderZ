from SpiderUtils.spider import Spider
from SpiderUtils.spiderStrategy import SpiderStrategy
from SpiderUtils.enums import Language
from Statics.wordCount import WordCount

s = SpiderStrategy("http://www.360doc.com/index.html", 2, True, None, Language.Chinese)
Spider(s).get_all_words()
WordCount.calc_count()
