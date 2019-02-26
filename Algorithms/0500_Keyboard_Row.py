class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first = set("qwertyuiop")
        second = set("asdfghjkl")
        third = set("zxcvbnm")
        
        result = []
        for word in words:
            w_set = set(word.lower())
            if (w_set.issubset(first) or
                    w_set.issubset(second) or
                    w_set.issubset(third)):
                result.append(word)
        return result
