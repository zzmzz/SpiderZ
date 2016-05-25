from enum import Enum


class Language(Enum):
    Chinese = 1
    English = 2
    Korean = 3

    @staticmethod
    def get_enum(num):
        return Language.__call__(num)
