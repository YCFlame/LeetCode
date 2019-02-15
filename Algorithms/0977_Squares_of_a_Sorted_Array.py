class Solution:
    def sortedSquares(self, A: 'List[int]') -> 'List[int]':
        result = list(range(len(A)))
        start, end = 0, len(A) - 1
        cur = end
        while start <= end:
            start_power = A[start] ** 2
            end_power = A[end] ** 2
            if start_power > end_power:
                result[cur] = start_power
                start += 1
            else:
                result[cur] = end_power
                end -= 1
                             
            cur -= 1
            
        return result
