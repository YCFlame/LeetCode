class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = [1]
        cur = 1
        while cur < n:
            temp = []
            last = result[0]
            count = 1
            for c in result[1:]:
                if c == last:
                    count += 1
                else:
                    temp.append(count)
                    temp.append(last)
                    last, count = c, 1
            else:
                temp.append(count)
                temp.append(last)
            result = temp
            cur += 1
        
        return ''.join(str(i) for i in result)
