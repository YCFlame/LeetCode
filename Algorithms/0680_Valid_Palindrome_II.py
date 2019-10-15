class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(i, j):
            return all(s[k] == s[j-k+i] for k in range(i, j))
        
        for i in range(len(s) // 2):         
            if s[i] != s[~i]:
                j = len(s) - 1 - i
                return is_palindrome(i, j - 1) or is_palindrome(i + 1, j)
        
        return True
