class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rs = 0
        cache = {}
        start = 0
        for i, c in enumerate(s):
            if c in cache:
                rs = max(rs, i - start)
                start = max(start, cache[c] + 1)
            
            cache[c] = i
                        
        return max(rs, len(s) - start)
