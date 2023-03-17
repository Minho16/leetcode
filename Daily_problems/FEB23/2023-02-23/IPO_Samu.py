from typing import List


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        left = 0
        right = sum(profits)
        while left < right:
            m = left + (right - left) // 2

        return left


s = Solution()
k = 2
w = 0
profits = [1, 2, 3]
capital = [0, 1, 1]
r = s.findMaximizedCapital(k, w, profits, capital)
print(r, r == 4)

k = 3
w = 0
profits = [1, 2, 3]
capital = [0, 1, 2]

r = s.findMaximizedCapital(k, w, profits, capital)
print(r, r == 6)
