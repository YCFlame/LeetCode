#! /usr/bin/env python
# coding: utf-8


class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        common_keys = set(c1.keys()) & set(c2.keys())
        result = []
        for k in common_keys:
            count = min(c1[k], c2[k])
            result.extend([k for i in range(count)])
        return result
