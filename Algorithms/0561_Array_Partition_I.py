"""
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        rs = 0
        for i in range(0, len(nums), 2):
            rs += nums[i]
        
        return rs
"""    

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        arr = [0] * 20001
        gap = 10000;
        for i in nums:
            arr[i + gap] += 1
            
        one_more = 0
        sum = 0
        for i in range(-10000, 10001):
            sum += (arr[i + gap] + 1 - one_more) // 2 * i
            one_more = (2 + arr[i + gap] - one_more) % 2
        return sum
