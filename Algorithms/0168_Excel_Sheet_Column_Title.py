class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = []
        base = ord('A')
        while n:               
            remain = (n - 1) % 26
            result.append(chr(remain + base))          
            n = (n - 1) // 26
        
        return ''.join(reversed(result))
