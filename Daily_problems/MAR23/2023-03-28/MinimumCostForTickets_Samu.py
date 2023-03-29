# 983. Minimum Cost For Tickets
from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        sum_vec = [0]*n
        for i in range(0, n):
            sum_vec[i] = sum_vec[i-1]+costs[0]
        i = 0
        while i < n:
            sum_vec[i] = min(sum_vec[i], sum_vec[i-1]+costs[0])
            j = i+1
            while j < n and days[j] < days[i]+7:
                if i == 0:
                    sum_vec[j] = min(sum_vec[j], costs[1])
                else:
                    sum_vec[j] = min(sum_vec[j], sum_vec[i-1]+costs[1])
                j += 1
            j = i+1
            while j < n and days[j] < days[i]+30:
                if i == 0:
                    sum_vec[j] = min(sum_vec[j], costs[2])
                else:
                    sum_vec[j] = min(sum_vec[j], sum_vec[i-1]+costs[2])
                j += 1
            i += 1

        return sum_vec[-1]

days = [1,4,6,7,8,20]
costs = [2,7,15] #11

days = [1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2,7,15]

days = [4,5,9,11,14,16,17,19,21,22,24]
costs = [1,4,18] # 10

days = [1,4,6,9,10,11,12,13,14,15,16,17,18,20,21,22,23,27,28]
costs = [3,13,45] #44
print(Solution().mincostTickets(days, costs))
# Input:
# Output: 11
