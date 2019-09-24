class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        rs = x ^ y
        count = 0
        while rs != 0:
            rs &= rs - 1
            count += 1
        
        return count
