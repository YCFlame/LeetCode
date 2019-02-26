class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 2:
            return N
        
        result = 0
        first, second = 0, 1
        while N > 1:
            result = first + second
            first, second = second, result
            N -= 1
        
        return result
