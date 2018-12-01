class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = result = nums[0]
        for i in nums[1:]:
            if current < 0:
                current = 0
            current += i
            if current > result:
                result = current
        
        return result
