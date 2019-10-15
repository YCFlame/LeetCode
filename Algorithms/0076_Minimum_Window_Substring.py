class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        rs = []
        cache = {}
        t = Counter(t)
        complete = 0
        start = 0
        for cur in range(len(s)):
            if s[cur] in t: 
                cache[s[cur]] = cache.get(s[cur], 0) + 1
                if cache[s[cur]] == t[s[cur]]:
                    complete += 1  
                    
                while start <= cur and complete == len(t):
                    if not rs or cur - start < rs[1] - rs[0]:
                        rs[:] = start, cur

                    if s[start] in t:
                        cache[s[start]] -= 1
                        if cache[s[start]] < t[s[start]]:
                            complete -= 1
                            
                    start += 1
        
        return s[rs[0]: rs[1] + 1] if rs else ""
