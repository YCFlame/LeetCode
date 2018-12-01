class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        start, end = 0, len(nums) - 1
        index = 0
        while index <= end:
            if nums[index] == 0 and index != start:
                nums[start], nums[index] = nums[index], nums[start]
                start += 1
            elif nums[index] == 2 and index != end:
                nums[end], nums[index] = nums[index], nums[end]
                end -= 1
            else:
                index += 1
