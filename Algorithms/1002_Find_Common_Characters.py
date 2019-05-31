class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        from collections import Counter
        result = Counter(A[0])
        for s in A[1:]:
            tmp = Counter(s)
            for k, v in result.items():
                if tmp[k] < v:
                    result[k] = tmp[k]
        
        common = []
        for k, v in result.items():
            for _ in range(v):
                common.append(k)
        
        return common
