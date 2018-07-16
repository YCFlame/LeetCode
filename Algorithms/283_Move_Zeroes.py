#! /usr/bin/env python
# coding: utf-8


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        last_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != last_index:
                    nums[last_index], nums[i] = nums[i], nums[last_index]
                last_index += 1
