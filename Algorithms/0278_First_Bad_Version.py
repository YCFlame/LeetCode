# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n + 1
        mid = (start + end) // 2
        while start < end:
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid 
                end = mid
            else:
                start = mid + 1
            
            mid = (start + end) // 2
            
        return mid
