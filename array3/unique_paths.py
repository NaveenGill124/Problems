#------------------A high time complexity approach----------------- using recursion-----------
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def path(i: int, j: int):
            
          if i == m-1 and j == n-1:
                return 1
            if i>=m or j>=n:
                return 0
            
            else:
                return path(i+1,j) + path(i,j+1)
        return path(0,0)

#------------------------------------------better approach------------using dynamic programming------------

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[-1]*n for _ in range(m)]
        # creates an m×n table filled with -1 to signal “not yet computed.”

        def path(i: int, j: int):
            
            if i>=m or j>=n:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]

            if i == m-1 and j == n-1:
                dp[i][j] = 1

            else:
                dp[i][j] = path(i+1,j) + path(i,j+1)
            
            return dp[i][j]

        return path(0,0)
#-------------------------------------Now optimal solution----------------------------------------

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        z = m+n-2
        a = m-1
        b = n-1
        result = 1

        for i in range(1,b+1):

            result = result * (z-b+i)//i
        return result


