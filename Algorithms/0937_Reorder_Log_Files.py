class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        alpha, num = [], []
        for log in logs:
            if log[-1].isalpha():
                alpha.append(log)
            else:
                num.append(log)
        return sorted(alpha, key=lambda l: ' '.join(l.split()[1:]))+ num
