from typing import List


class Solution:
    # O(k) solution | Runtime: 49 ms (86.17%) | Memory: 14 MB (44.89%)
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i = 0
        val = 1
        while k > 0:
            if i < len(arr):
                if arr[i] > val:
                    k -= 1
                else:
                    i += 1
                val += 1
            else:
                val += k
                k = 0
        return val - 1


s = Solution()
r = s.findKthPositive([2, 3, 4, 7, 11], 5)
print(r, r == 9)

r = s.findKthPositive([1, 2, 4], 6)
print(r, r == 6)
