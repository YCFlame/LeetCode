class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        last = 0
        for i in range(len(nums)):
            if nums[i] != val:
                if i != last:
                    nums[last] = nums[i]
                last += 1
        
        return last
