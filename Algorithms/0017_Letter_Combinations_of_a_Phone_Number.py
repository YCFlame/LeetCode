class Solution:
    mapper = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }
    def letterCombinations(self, digits: str) -> List[str]:
        rs = []
        for d in digits:
            if not rs:
                rs = self.mapper[d]
            else:
                rs = [prefix + c for prefix in rs for c in self.mapper[d]]
        
        return rs
