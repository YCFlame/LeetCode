class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while temp << 1 <= dividend:
                i <<= 1
                temp <<= 1
            
            dividend -= temp
            res += i

        if not positive:
            res = -res
            
        return min(max(-2147483648, res), 2147483647)
