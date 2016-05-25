from bson.code import Code
import pymongo
from Utils.config import Config
from Utils.logFactory import LogFactory

class WordCount:
    logger = LogFactory.getlogger("WordCount")

    mapper = Code("""
        function() {
            emit(this.content, 1);
        }
    """)

    reducer = Code("""
        function(key, values) {
            var sum = 0;
            values.forEach(function(value) {
                sum += Number(value);
            });
            return sum;
        };
    """)

    @staticmethod
    def calc_count():
        WordCount.logger.info("start to count words")
        ip = Config.getProperty('mongo', 'addr')
        port = int(Config.getProperty('mongo', 'port'))
        client = pymongo.MongoClient(ip, port)
        db = client.spiderDB
        collection = db.spider
        collection.map_reduce(WordCount.mapper, WordCount.reducer, out="result", full_response=True)
