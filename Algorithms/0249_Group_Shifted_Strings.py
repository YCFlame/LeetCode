class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        map = {}
        for s in strings: 
            key = 0
            for i in range(1, len(s)):
                key *= 100
                key += (ord(s[i]) - ord(s[i - 1]) + 26) % 26 + 1
            map.setdefault(key, []).append(s)
        
        return list(map.values())
