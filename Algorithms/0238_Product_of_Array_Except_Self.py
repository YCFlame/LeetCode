class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rs = [0] * len(nums)
        rs[0] = 1
        for i in range(1, len(nums)):
            rs[i] = rs[i - 1] * nums[i - 1]
        
        R = 1
        for i in range(len(nums) - 1, -1, -1):
            rs[i] = R * rs[i]
            R *= nums[i]
            
        return rs
