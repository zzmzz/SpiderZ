from bson.code import Code
import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client.spiderDB
collection = db.spider
collection.remove()


class WordCount:
    mapper = Code("""
        function() {
            emit(this.content, {count: 1});
        }
    """)

    reducer = Code("""
        function(key, values) {
            var sum = 0;
            values.forEach(function(value) {
                sum += value['count'];
            });
            return {count:sum};
        };
    """)

    @staticmethod
    def calc_count():
        collection.map_reduce(WordCount.mapper, WordCount.reducer, out="result", full_response=True)
