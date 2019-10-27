class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []
        def backtrack(first):
            if first == n:
                output.append(nums[:])
            
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        backtrack(0)
        return output
