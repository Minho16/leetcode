from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # How to solve the problem
        # Looks like an easy problem
        # We need to divide all the piles in groups of len 'h'
        # Let's try agai binary search
        # A maximum value of k can be the maximum value of k
        if len(piles) == 1:
            c = piles[0] // h
            if piles[0] % h > 0:
                c += 1
            return c
        r = max(piles)
        l = 0
        while l < r:
            m = l + (r - l) // 2
            c = 0

            for i in piles:
                c += i // m
                if i % m > 0:
                    c += 1
            if c <= h:
                r = m
            else:
                l = m + 1
        return l


s = Solution()
r = s.minEatingSpeed([3, 6, 7, 11], 8)
print(r, r == 4)

r = s.minEatingSpeed([30, 11, 23, 4, 20], 5)
print(r, r == 30)

r = s.minEatingSpeed([30, 11, 23, 4, 20], 6)
print(r, r == 23)
