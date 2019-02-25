class Solution:
    def isHappy(self, n: int) -> bool:
        result = set()
        while True:
            tmp = 0
            while n:
                tmp += (n % 10) ** 2
                n = n // 10
            
            if tmp == 1:
                return True
            elif tmp in result:
                return False
            
            result.add(tmp)
            n = tmp
