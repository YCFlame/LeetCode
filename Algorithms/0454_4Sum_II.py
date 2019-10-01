class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        from collections import Counter
        cache = Counter()
        for a in A:
            for b in B:
                cache[a + b] += 1
        
        rs = 0
        for c in C:
            for d in D:
                rs += cache[-(c + d)]
                    
        return rs
