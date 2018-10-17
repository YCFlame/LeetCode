class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        index = s.rfind(' ')
        return len(s) - index - 1
