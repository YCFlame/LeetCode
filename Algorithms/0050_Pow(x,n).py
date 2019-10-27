class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0 :
            x = 1 / x
            n = -n
        
        ans = 1
        current_product = x
        i = n
        while i > 0:
            if i & 1:
                ans = ans * current_product
            
            current_product = current_product * current_product
            i >>= 1
        
        return ans
