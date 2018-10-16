#! /usr/bin/env python
# coding: utf-8

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        last = 0
        for i in range(1, len(nums)):
            if nums[last] != nums[i]:
                last += 1
                if last != i:
                    nums[last] = nums[i]

        return last + 1
