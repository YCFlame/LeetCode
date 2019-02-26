class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = set(J)
        return len([c for c in S if c in jewels])
