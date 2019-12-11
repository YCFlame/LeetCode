class Solution:
    def countSubstrings(self, s: str) -> int:
        if not s:
            return []
        
        rs = 0
        def expand(s, left, right):
            nonlocal rs
            while left >= 0 and right < len(s) and s[left] == s[right]:
                rs += 1
                left -= 1
                right += 1

            return right - left - 1
        
        for i in range(len(s)):
            expand(s, i, i)
            expand(s, i, i + 1)
        
        return rs
