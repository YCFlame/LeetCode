class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')
        result = []
        for i, w in enumerate(S.split()):
            if w[0] in vowels:
                result.append(w + 'ma' + (i + 1) * 'a')
            else:
                result.append(w[1:] + w[0] + 'ma' + (i + 1) * 'a')
        return ' '.join(result)
