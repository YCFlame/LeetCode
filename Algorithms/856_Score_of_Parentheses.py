#! /usr/bin/env python
# coding: utf-8

class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int

        Given a balanced parentheses string S, compute the score of the string based on the following rule:
        1. () has score 1
        2. AB has score A + B, where A and B are balanced parentheses strings.
        3. (A) has score 2 * A, where A is a balanced parentheses string.
        """
        stack = []
        result = 0
        for i in S:
            if i == '(':
                stack.append(i)
            else:
                j = stack.pop()
                count = 0
                while stack and j != '(':
                    count += j
                    j = stack.pop()
                stack.append(2 * count if count > 0 else 1)
        return sum(stack)
