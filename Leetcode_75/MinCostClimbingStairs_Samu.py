from typing import List
# Linear complexity solution (Runtime: 47 ms (99.28%) | Memory: 14.1 MB)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        f1 = cost[0]
        f2 = cost[1]
        for v in cost[2:]:
            if f1 < f2:
                f1, f2 = f2, f1+v
            else:
                f1, f2 = f2, f2+v
        return min(f1, f2)

s = Solution()
cost: List = [10,15,20]
r = s.minCostClimbingStairs(cost)
print(r, r==15)

cost: List = [1,100,1,1,1,100,1,1,100,1]
r = s.minCostClimbingStairs(cost)
print(r, r==6)

cost: List = [0,2,2,1]
r = s.minCostClimbingStairs(cost)
print(r, r==2)