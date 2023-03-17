from collections import deque
import numpy as np


class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        pos = deque([[sr, sc]])
        c0 = image[sr][sc]
        image[sr][sc] = color
        m = len(image)
        n = len(image[0])
        first_time = np.full((m, n), True)
        while len(pos) > 0:
            x, y = pos.popleft()
            if image[min(x + 1, m - 1)][y] == c0 and first_time[min(x + 1, m - 1)][y]:
                first_time[min(x + 1, m - 1)][y] = False
                image[min(x + 1, m - 1)][y] = color
                pos.append([min(x + 1, m - 1), y])
            if image[max(0, x - 1)][y] == c0 and first_time[max(0, x - 1)][y]:
                first_time[max(0, x - 1)][y] = False
                image[max(0, x - 1)][y] = color
                pos.append([max(0, x - 1), y])

            if image[x][min(y + 1, n - 1)] == c0 and first_time[x][min(y + 1, n - 1)]:
                first_time[x][min(y + 1, n - 1)] = False
                image[x][min(y + 1, n - 1)] = color
                pos.append([x, min(y + 1, n - 1)])
            if image[x][max(0, y - 1)] == c0 and first_time[x][max(0, y - 1)]:
                first_time[x][max(0, y - 1)] = False
                image[x][max(0, y - 1)] = color
                pos.append([x, max(0, y - 1)])
        return image
