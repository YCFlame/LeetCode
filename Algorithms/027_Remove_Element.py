class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        start = 0
        for i in range(len(nums)):
            if nums[i] != val:
                if i != start:
                    nums[start], nums[i] = nums[i], nums[start]
                start += 1
        
        nums = nums[:start]
        return start
