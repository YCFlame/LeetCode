class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        result = anchor = 0
        for i in range(len(nums)):
            if i and nums[i - 1] >= nums[i]:
                anchor = i
            
            result = max(result, i - anchor + 1)
       
        return result
