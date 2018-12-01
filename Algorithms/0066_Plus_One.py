#! /usr/bin/env python
# coding: utf-8


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = False
        for i in range(-1, -len(digits) - 1, -1):
            if i == -1 or carry:
                d = digits[i] + 1
                if d == 10:
                    carry = True
                    digits[i] = 0
                else:
                    carry = False
                    digits[i] = d
                    break
        if carry:
            digits.insert(0, 1)

        return digits
