class Solution:
    def isPowerOfThree(self, n: 'int') -> 'bool':      
        if n == 1:
            return True
        tmp = 3
        while tmp < n:
            tmp *= 3
        return tmp == n
