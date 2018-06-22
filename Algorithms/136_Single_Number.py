#! /usr/bin/env python
# coding: utf-8


class Solution(object):
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result = A[0]
        for x in A[1:]:
            result ^= x

        return result
