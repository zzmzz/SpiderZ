import jieba


class SplitProxy:
    __split_tool = None

    def __init__(self):
        self.__split_tool = jieba;

    def split(self, str):
        word_list = jieba.cut(str, True);
        return word_list
