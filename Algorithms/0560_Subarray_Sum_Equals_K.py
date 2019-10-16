class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cache = {0: 1}
        sum = 0
        count = 0
        for n in nums:
            sum += n
            count += cache.get(sum - k, 0)
            cache[sum] = cache.get(sum, 0) + 1
        
        return count
