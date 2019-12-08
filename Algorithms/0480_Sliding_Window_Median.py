from collections import Counter
from heapq import heappush, heappop

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if not nums:
            return 0
        
        lo, hi = [], []
        for i in range(k):
            heappush(lo, -nums[i])
        
        for i in range(k // 2):
            heappush(hi, -heappop(lo))
        
        odd = bool(k & 1)
        medians = [-lo[0] if odd else (hi[0] - lo[0]) / 2]
        
        cache = Counter()

        for i in range(k, len(nums)):
            outgo = nums[i - k]
            income = nums[i]
            balance = 0
            
            balance += -1 if outgo <= -lo[0] else 1
            cache[outgo] += 1
            
            if lo and income <= -lo[0]:
                balance += 1
                heappush(lo, -income)
            else:
                balance -= 1
                heappush(hi, income)
            
            if balance < 0:
                heappush(lo, -heappop(hi))
                balance += 1
            elif balance > 0:
                heappush(hi, -heappop(lo))
                balance -= 1
            
            while cache[-lo[0]]:
                cache[-lo[0]] -= 1
                heappop(lo)
            
            while hi and cache[hi[0]]:
                cache[hi[0]] -= 1
                heappop(hi)
            
            medians.append(-lo[0] if odd else (hi[0] - lo[0]) / 2)
        
        return medians
