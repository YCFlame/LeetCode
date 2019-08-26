class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:   
        cache = {}
        rs = 0
        start = 0
        for i, c in enumerate(s):
            if c in cache:
                start = max(cache[c] + 1, start)

            rs = max(rs, i - start + 1)
            cache[c] = i
        return rs
