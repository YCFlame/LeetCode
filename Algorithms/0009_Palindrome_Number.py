#! /usr/bin/env python3
# coding: utf-8

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        x = str(x)
        return x == x[::-1]
