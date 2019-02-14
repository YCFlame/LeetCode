class Solution:
    def isPowerOfFour(self, num: 'int') -> 'bool':
        import math
        if num < 1:
            return False
        return math.log(num, 4).is_integer()
