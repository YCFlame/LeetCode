#! /usr/bin/env python
# coding: utf-8

class Solution(object):
    # @return an integer
    def reverse(self, x):
        result = int(str(abs(x))[::-1])
        return -result if x < 0 else result
