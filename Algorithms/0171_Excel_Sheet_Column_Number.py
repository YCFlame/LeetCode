class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        result = 0
        N = len(s)
        base = ord('A')
        while count < N:
            result += (ord(s[N - 1 - count]) - base + 1) * (26 ** count)
            count += 1    
        return result
