class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        gap = (sum(A) -sum(B)) // 2
        B = set(B)
        for i in A:
            match = i - gap
            if match in B:
                return [i, match]
