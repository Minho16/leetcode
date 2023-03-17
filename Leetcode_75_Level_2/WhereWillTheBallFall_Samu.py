from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        cols = []
        for i in range(len(grid[0])):
            y = i
            x = 0
            roll = True
            while roll:
                if grid[x][y] == -1:
                    if y - 1 < 0 or grid[x][y - 1] == 1:
                        roll = False
                        cols.append(-1)
                    else:
                        y -= 1
                        x += 1
                else:
                    if y + 1 >= len(grid[0]) or grid[x][y + 1] == -1:
                        roll = False
                        cols.append(-1)
                    else:
                        y += 1
                        x += 1
                if x == len(grid):
                    roll = False
                    cols.append(y)
        return cols
