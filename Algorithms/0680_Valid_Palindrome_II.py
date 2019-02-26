class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] != s[end]:
                first, second = s[start: end], s[start + 1:end + 1]
                return first == first[::-1] or second == second[::-1]
            
            start += 1
            end -= 1
                
        return True
