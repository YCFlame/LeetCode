class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import Counter
        c = Counter()
        lo = 0
        imax = 0
        length = 0
        for hi in range(len(s)):
            c[s[hi]] += 1
            imax = max(imax, c[s[hi]])
            while hi - lo + 1 - imax > k:
                c[s[lo]] -= 1
                lo += 1

        # no need to lower imax because the old one ensure the smallest sliding window even it's invalid
        # so we can calculate the length as follows
        return len(s) - lo
