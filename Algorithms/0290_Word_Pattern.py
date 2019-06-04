class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if len(pattern) != len(words):
            return False
        
        mapper = {}
        unique = set()
        for c, w in zip(pattern, words):
            if w not in mapper:
                if c not in unique:
                    mapper[w] = c
                    unique.add(c)
                else:
                    return False
            elif mapper[w] != c:
                return False
            
        return True
