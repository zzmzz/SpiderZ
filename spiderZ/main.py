from SpiderUtils.spider import Spider
from SpiderUtils.spiderStrategy import SpiderStrategy
from SpiderUtils.enums import Language
s=SpiderStrategy("http://www.baidu.com/s?tn=mswin_oem_dg&ie=utf-16&word=%E7%99%BE%E5%BA%A6%E9%A6%96%E9%A1%B5%E6%8A%93%E4%B8%8D%E5%88%B0%E4%B8%AD%E6%96%87",2,True,"baidu",Language.Chinese)
Spider(s).get_all_words()