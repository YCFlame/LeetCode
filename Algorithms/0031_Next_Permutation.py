class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tp = len(nums) - 2
        while tp >= 0 and nums[tp] >= nums[tp + 1]:
            tp -= 1
        
        if tp >= 0:
            swap = len(nums) - 1
            while swap >= 0 and nums[swap] <= nums[tp]:
                swap -= 1
            nums[tp], nums[swap] = nums[swap], nums[tp]
            
        start, end = tp + 1, len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
