import numpy as np
from collections import deque


class Solution(object):
    m, n = 0, 0
    explored = np.zeros((m, n))
    grid = np.zeros((m, n))

    def cover_island(self, x, y):
        if x < 0 or y < 0 or x >= Solution.m or y >= Solution.n:
            return
        else:
            if Solution.grid[x][y] == "1" and Solution.explored[x][y] == 0:
                Solution.explored[x][y] = 1
                self.cover_island(x + 1, y)
                self.cover_island(x - 1, y)
                self.cover_island(x, y + 1)
                self.cover_island(x, y - 1)
        return

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        Solution.m, Solution.n = len(grid), len(grid[0])
        Solution.explored = np.zeros((Solution.m, Solution.n))
        Solution.grid = grid
        land = deque()
        for i in range(Solution.m):
            for j in range(Solution.n):
                if Solution.grid[i][j] == "1":
                    land.append([i, j])
        island = 0
        while land:
            x, y = land.popleft()
            if not Solution.explored[x][y]:
                self.cover_island(x, y)
                island += 1
        print(island)
        return island


s = Solution()
grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]
r = s.numIslands(grid)


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"],
]
r = s.numIslands(grid)
print(r, r == 3)
