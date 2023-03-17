from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            can = True
            d = 1
            t = 0
            for w in weights:
                t += w
                if t > mid:
                    t = w
                    d += 1
                    if d > days:
                        can = False
                        break
            if can:
                right = mid
            else:
                left = mid + 1
        return left


s = Solution()
r = s.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
print(r, r == 15)

r = s.shipWithinDays([3, 2, 2, 4, 1, 4], 3)
print(r, r == 6)

r = s.shipWithinDays([1, 2, 3, 1, 1], 4)
print(r, r == 3)
