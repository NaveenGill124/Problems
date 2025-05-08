
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m = len(matrix)
        n =  len(matrix[0])
        # let's store zero's postion first

        zero_list = []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_list.append((i,j))
    
        for i,j in zero_list:
            
            # zero out row i
            for col in range(n):
                matrix[i][col] = 0
                
            # zero out row j
            for row in range(m):
                matrix[row][j] = 0


