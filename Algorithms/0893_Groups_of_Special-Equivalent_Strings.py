class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        result = set()
        for word in A:
            result.add((''.join(sorted(word[::2])) + ''.join(sorted(word[1::2]))))
    
        return len(result)
    
    
"""
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        result = set()
        for word in A:
            fingerprint = [0 for i in range(52)]
            for i, c in enumerate(word):
                fingerprint[ord(c) - ord('a') + 26 * (i % 2)] += 1
            
            result.add(tuple(fingerprint))
        
        return len(result)
"""
