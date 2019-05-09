class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = [s[i: i + k] for i in range(0, len(s), k)]
        for i in range(0, len(result), 2):
            result[i] = result[i][::-1]
            
        return ''.join(result)
