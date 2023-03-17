import time
from typing import List


class Solution:
    # First version O(nlog(n)) complexity. TLE in leetcode..........
    # Bad algoithm --> Does not implement properly the notions of binary search
    # Too many lines of code
    # Too many variables
    # Too many ifs and returns
    # Bad 'l' reassignation --> never stops while condition
    #                       --> Use 'l' = m+1 insted
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        r = max(time) * totalTrips
        l = 0
        while l < r:
            c_r = 0
            c_l = 0
            c_m = 0
            m = l + (r - l) // 2
            c_r1 = 0
            c_l1 = 0
            c_m1 = 0
            for i in time:
                c_r += r // i
                c_l += l // i
                c_m += m // i
                c_r1 += (r - 1) // i
                c_l1 += (l - 1) // i
                c_m1 += (m - 1) // i
            if c_r >= totalTrips and c_r1 < totalTrips:
                return r
            elif c_l >= totalTrips and c_l1 < totalTrips:
                return l
            elif c_m >= totalTrips and c_m1 < totalTrips:
                return m

            if c_m >= totalTrips:
                r = m
            else:
                l = m
        return l

    # Second version after revising the Binary search algorithm
    # This version is only a few times faster but the same overall O(nlog(n)) time complexity
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        r = max(time) * totalTrips
        l = 0

        while l < r:
            m = l + (r - l) // 2
            c_m = 0
            for i in time:
                c_m += m // i

            if c_m >= totalTrips:
                r = m
            else:
                l = m + 1
        return l


s = Solution()
r = s.minimumTime([1], 4)
print(r, r == 4)

r = s.minimumTime([1, 2, 3], 5)
print(r, r == 3)

r = s.minimumTime([5, 10, 10], 9)
print(r, r == 25)

r = s.minimumTime([3, 3, 8], 6)
print(r, r == 9)
