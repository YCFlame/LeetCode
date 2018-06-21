#! /usr/bin/env python
# coding: utf-8

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = 0
        last = None
        for i in range(len(nums)):
            if last != nums[i]:
                last = nums[i]
                if length > 0:
                    nums[length], nums[i] = nums[i], nums[length]
                length += 1

        nums = nums[:length]
        return length
