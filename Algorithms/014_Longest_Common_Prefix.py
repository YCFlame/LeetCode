class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if not strs:
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        common = []
        i = 0
        for i in range(len(strs[0])):
            c = strs[0][i]
            for s in strs[1:]:   
                if i >= len(s) or s[i] != c:
                    return ''.join(common)
                
            common.append(c)
        
        return ''.join(common)
