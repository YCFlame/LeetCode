class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        rs = len(nums) + 1
        start = 0
        length = 0
        cur = 0
        for i in range(len(nums)):
            cur += nums[i]
            while cur >= s:
                rs = min(rs, i - start + 1)
                cur -= nums[start]
                start += 1

        return rs if rs <= len(nums) else 0
