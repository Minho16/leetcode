import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def check_if_possible_with_h(mid) -> bool:
            hours = 0
            for bananas in piles:
                hours += math.ceil(bananas / mid)
            return hours <= h

        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2

            is_possible = check_if_possible_with_h(mid)

            if is_possible:
                right = mid
            else:
                left = mid + 1

        return right
