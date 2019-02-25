class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        from collections import Counter
        counter = Counter(A.split() + B.split())
        return [i for i, c in counter.items() if c == 1]
