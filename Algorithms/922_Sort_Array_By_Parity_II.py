class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j, length = 0, 1, len(A)
        while True:
            while i < length and A[i] % 2 == 0:
                i += 2
            while j < length and A[j] % 2 == 1:
                j += 2
                
            if not (i < length and j < length):
                break
                
            A[i], A[j] = A[j], A[i]   
        
        return A
