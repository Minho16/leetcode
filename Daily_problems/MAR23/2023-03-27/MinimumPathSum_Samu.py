# 64. Minimum Path Sum
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                min_v = 1000
                if i == 0 and j > 0:
                    grid[i][j] = grid[i][j] + grid[i][j-1]
                elif j == 0 and i > 0:
                    grid[i][j] = grid[i][j] + grid[i-1][j]
                elif j > 0 and i > 0:
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1])+grid[i][j]
        return grid[-1][-1]
