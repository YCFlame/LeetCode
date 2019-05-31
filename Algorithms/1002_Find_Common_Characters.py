class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        from collections import Counter
        result = Counter(A[0])
        for s in A[1:]:
            result &= Counter(s)
        
        return list(result.elements())
