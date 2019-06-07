class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if not self.min or x <= self.min[-1]:
            self.min.append(x)

    def pop(self):
        """
        :rtype: None
        """

        r = self.stack.pop()
        if self.min and self.min[-1] == r:
            self.min.pop()
        
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]
