class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = 0
        for i in range(len(arr)):
            if i + zeros >= len(arr):
                break
                
            if arr[i] == 0:
                zeros += 1
            
        for j in range(i - 1, -1, -1):
            if zeros == 0:
                break
            
            if j + zeros < len(arr):
                arr[j + zeros] = arr[j]
            
            if arr[j] == 0:
                zeros -= 1
                arr[j + zeros] = 0
   
