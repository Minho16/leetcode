# 54. Spiral Matrix
from typing import List


class Solution:
    # O(nxm) time complexity | Runtime: 28 ms (85.55%),  Memory: 13.8 MB (72.74%)
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # x being the first element in the matrix and y being the second one
        max_x = len(matrix)
        max_y = len(matrix[0])
        min_x = 0
        min_y = 0
        spiral = []
        while min_x < max_x and min_y < max_y:
            for i in range(min_y, max_y):
                spiral.append(matrix[min_x][i])
            min_x += 1
            for i in range(min_x, max_x):
                spiral.append(matrix[i][max_y - 1])
            max_y -= 1
            if min_x < max_x:
                for i in range(max_y - 1, min_y - 1, -1):
                    spiral.append(matrix[max_x - 1][i])
                max_x -= 1
            if min_y < max_y:
                for i in range(max_x - 1, min_x - 1, -1):
                    spiral.append(matrix[i][min_y])
                min_y += 1
        return spiral
