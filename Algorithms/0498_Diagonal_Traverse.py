class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        up = True
        i = j = 0
        m = len(matrix)
        n = len(matrix[0])
        rs = []
        while i < m and j < n:
            rs.append(matrix[i][j])
            if up:
                if i == 0 or j == n - 1:
                    up = False
                    if j == n - 1:
                        i += 1
                    else:
                        j += 1
                else:
                    i -= 1
                    j += 1
                        
            else:
                if i == m - 1 or j == 0:
                    up = True
                    if i == m - 1:
                        j += 1
                    else:
                        i += 1
                        
                else:   
                    i += 1
                    j -= 1
        
        return rs
