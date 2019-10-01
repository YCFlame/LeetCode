class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rs = [0] * (rowIndex + 1)
        rs[0] = 1
        
        for i in range(1, rowIndex + 1):
            for j in range(i, 0, -1):
                rs[j] += rs[j - 1]
     
        return rs
