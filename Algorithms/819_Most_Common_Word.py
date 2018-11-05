class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        from collections import Counter
        words = Counter()
        banned = set(banned)
        w = []
        for c in paragraph:
            if c.isalpha():
                w.append(c)
            elif w:
                word = ''.join(w).lower()
                if word not in banned:
                    words[word] += 1
                
                w = []
        
        if w:
            word = ''.join(w).lower()
            if word not in banned:
                words[word] += 1
        
        return words.most_common(1)[0][0]
