from typing import List
class Solution:
    # Wrong approach
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 0
        val = 1
        while k > 0:
            if i < len(arr) and arr[i] > val:
                val += 1
            elif i < len(arr):
                k -= 1
            else:
                val += 1
                k -= 1
            i+= 1
        return val
