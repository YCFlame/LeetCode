class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        dual_center = ["11","69","88","96", "00"]
        single_center = ["0", "1", "8"]
        if n == 1:
            return single_center
        if n == 2:
            return dual_center[:-1]
        if n % 2:
            pre, center = self.findStrobogrammatic(n-1), single_center
        else: 
            pre, center = self.findStrobogrammatic(n-2), dual_center
        mid = (n - 1) // 2
        return [p[:mid] + c + p[mid:] for c in center for p in pre]
