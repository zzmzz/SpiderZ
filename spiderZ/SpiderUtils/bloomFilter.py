#!/usr/bin/python
# coding=utf-8

from pybloomfilter import BloomFilter


class SpiderBloomFilter:
    filter_name = 'filter.bloom'

    def __init__(self, amount=1 << 26):
        BloomFilter(amount, 0.01, SpiderBloomFilter.filter_name)
        return

    @staticmethod
    def exists(value):
        bf = BloomFilter.open(SpiderBloomFilter.filter_name)
        return bf.add(value)