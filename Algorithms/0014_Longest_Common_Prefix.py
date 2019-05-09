class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        count = 0
        while True:
            for i in range(len(strs)):
                if count == len(strs[i]) or strs[i][count] != strs[0][count]:
                    return strs[0][:count]
            
            count += 1
