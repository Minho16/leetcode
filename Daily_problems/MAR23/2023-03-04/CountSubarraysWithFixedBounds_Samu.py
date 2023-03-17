from typing import List


class Solution:
    # Bad understanding of the problem
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        i = 0
        counter = 0
        while i < len(nums):
            j = i
            while j < len(nums):
                if nums[i] == minK and nums[j] == maxK:
                    counter += 1
                j += 1
            i += 1
        return counter


s = Solution()
r = s.countSubarrays([1, 2, 3, 4, 5, 6, 5], 1, 5)
print(r, r == 2)

r = s.countSubarrays([1, 1, 1, 1], 1, 1)
print(r, r == 10)


r = s.countSubarrays([1] * 10000, 1, 1)
print(r, r == 10)
