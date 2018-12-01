#! /usr/bin/env python
# coding: utf-8


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        count = 0
        for i in range(len(nums)):
            prev = nums[i]
            current = i
            while True:
                next = (current + k) % len(nums)
                tmp = nums[next]
                nums[next] = prev
                prev = tmp
                current = next
                count += 1
                if current == i:
                    break

            if count == len(nums):
                return


"""
        k = k % len(nums)
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)

def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
"""
