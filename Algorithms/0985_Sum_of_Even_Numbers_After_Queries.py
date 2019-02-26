class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        even_sum = 0
        for i in A:
            if i % 2 == 0:
                even_sum += i
        
        for value, index in queries:
            current = A[index]
            now = current + value
            if now % 2 == 0:
                even_sum += now
            
            if current % 2 == 0:
                even_sum -= current
            
            A[index] = now
            result.append(even_sum)
        
        return result
