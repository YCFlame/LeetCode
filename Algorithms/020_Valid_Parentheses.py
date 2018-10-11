class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapper = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        for c in s:
            if c in mapper:
                if not stack or stack[-1] != mapper[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0
