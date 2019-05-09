class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        first, second = 0, 1
        if nums[first] < nums[second]:
            first, second = second, first
            
        for i in range(2, len(nums)):
            if nums[i] > nums[first]:
                first, second = i, first
            elif nums[i] > nums[second]:
                second = i
        
        return first if nums[first] >= 2 * nums[second] else -1
            
