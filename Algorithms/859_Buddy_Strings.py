#! /usr/bin/env python
# coding: utf-8

class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool

        Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

        Input: A = "ab", B = "ba"
        Output: true

        Input: A = "ab", B = "ab"
        Output: false

        Input: A = "aa", B = "aa"
        Output: true

        """
        if len(A) != len(B):
            return False

        diff = []
        same, unique = False, set()
        for i in range(len(A)):
            if A[i] != B[i]:
                if len(diff) == 2:
                    return False
                else:
                    diff.append((A[i], B[i]))
            else:
                if A[i] in unique:
                    same = True
                else:
                    unique.add(A[i])

        if (len(diff) == 0 and same) or (len(diff) == 2 and diff[0][0] == diff[1][1] and diff[0][1] == diff[1][0]):
            return True

        return False
