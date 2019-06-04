class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapper = {}
        unique = set()
        for i in range(len(s)):
            if s[i] not in mapper:
                if t[i] not in unique:
                    mapper[s[i]] = t[i]
                    unique.add(t[i])
                else:
                    return False
            elif mapper[s[i]] != t[i]:
                return False
            
        return True
