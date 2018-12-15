class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        
        n1 = 1
        n2 = 2
        for _ in range(n - 2):
            result = n1 + n2
            n1 = n2
            n2 = result
            
        return result
