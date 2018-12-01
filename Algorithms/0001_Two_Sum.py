#! /usr/bin/env python
# coding: utf-8


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        partners = {}
        for i, n in enumerate(nums):
            partner = target - n
            if partner in partners:
                return [partners[partner], i]
            else:
                partners[n] = i
