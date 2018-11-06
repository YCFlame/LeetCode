class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        words = S.split(C)
        first = words[0]
        result = [i for i in range(len(first), 0, -1)]
        for w in words[1:-1]:
            result.extend([i for i in range((len(w) + 1)// 2 + 1)])
            result.extend([i for i in range(len(w) // 2, 0, -1)])
        
        result.extend([i for i in range(len(words[-1]) + 1)])
                
        return result
