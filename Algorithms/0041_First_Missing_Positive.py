class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while (0 < nums[i] <= len(nums)) and nums[nums[i] - 1] != nums[i]:
                n = nums[i]
                nums[i], nums[n - 1] = nums[n - 1], nums[i]
        
        for i, n in enumerate(nums):
            if n != i + 1:
                return i + 1
        
        return len(nums) + 1
