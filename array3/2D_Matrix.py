class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m =len(matrix)
        n = len(matrix[0])
        l = 0
        u = m*n-1 # because que says we have sorted numbers and we can asssum all like 1-D array

        while l<=u:
            mid = (l+u)//2
            i = mid // n # row
            j = mid % n    # column

            if target == matrix[i][j]:
                    return True
            else:
                if target > matrix[i][j]:
                    l = mid+1
                else:
                    u = mid-1 
                
        return False
