from typing import List
import heapq
class Solution:
    # O(n) solution (Runtime: 29 ms (86.51%) | Memory: 13.9 MB (50.96%))
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) > 0:
            if len(stones) == 1:
                return -stones[0]
            x = heapq.heappop(stones)
            if len(stones) == 0:
                return -x
            y =  heapq.heappop(stones)
            if x != y:
                heapq.heappush(stones, -abs(x-y))
        return 0
    
s = Solution()
r = s.lastStoneWeight([2,7,4,1,8,1])
print(r, r==1)