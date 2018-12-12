class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        from math import sqrt, trunc
        return trunc(sqrt(x))
