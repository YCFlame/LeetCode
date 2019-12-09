class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mapper = {
            "6": "9",
            "0": "0",
            "8": "8",
            "1": "1",
            "9": "6",
        }
        l, h = 0, len(num) - 1
        while l <= h:
            if not (mapper.get(num[l]) == num[h]):
                return False
            
            l += 1
            h -= 1
        
        return True
