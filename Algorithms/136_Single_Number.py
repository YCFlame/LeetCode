#! /usr/bin/env python
# coding: utf-8

class Solution(object):
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        for x in A[1:]:
            A[0] ^= x

        return A[0]
