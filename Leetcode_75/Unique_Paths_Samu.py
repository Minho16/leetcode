import numpy as np
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = np.zeros((m, n))

        grid[m-1][n-1] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i+1 < m and j+1 < n:
                    grid[i][j] = grid[i+1][j]+grid[i][j+1]
                elif i+1 < m:
                    grid[i][j] = grid[i+1][j]
                elif j+1 < n:
                    grid[i][j] = grid[i][j+1]
        return int(grid[0][0])
    
# Not DP but O(1) space complexity solution.
from math import factorial

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        rows, cols = m, n
        
        # from start to destination, we need (m-1) ↓ moves and (n-1) → moves
        # Thus, the number of unique paths is the number of permutations of (m-1) ↓ and (n-1) →
        #
        # Number of unique paths = ( m-1 + n-1 ) ! / (m-1)! * (n-1)!
        
        
        return factorial( m+n-2 ) // ( factorial( m-1 ) * factorial( n-1 ) ) 

# DP solution
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        rows, cols = m, n
        
        path_dp = [ [ 1 for j in range(cols)] for i in range(rows) ]
        
        
        # Dynamic Programming relation:
        
        # Base case:
        # DP(0, j) = 1 , only reachable from one step left
        # DP(i, 0) = 1 , only reachable from one step up
        
        # General case:
        # DP(i,j) = number of path reach to (i, j)
        #         = number of path reach to one step left + number of path reach to one step up
        #         = number of path reach to (i, j-1) + number of path to (i-1, j)
        #         = DP(i, j-1) + DP(i-1, j)
        
        
        
        for i in range(1, rows):
            for j in range(1, cols):
                
                path_dp[i][j] = path_dp[i][j-1] + path_dp[i-1][j]
        
        
        # Destination coordination = (rows-1, cols-1)
        return path_dp[rows-1][cols-1]


s = Solution()
r = s.uniquePaths(3, 7)
print(r, r==28)

r = s.uniquePaths(3, 2)
print(r, r==3)

r = s.uniquePaths(13,13)
print(r, r==1)