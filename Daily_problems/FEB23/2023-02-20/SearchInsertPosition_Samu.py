from typing import List


class Solution:
    # Binary search solution O(log(n)) complexity (Runtime: 54 ms (55.31%) | Memory: 14.8 MB (31.40%))
    # The fastest approach uses only the while block, using the pivot to compare the target value and properly updating the left and right values.
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        n = len(nums)
        if n == 0:
            return 0
        if nums[0] >= target:
            return 0
        elif nums[n - 1] == target:
            return n - 1
        elif nums[n - 1] < target:
            return n

        while True:
            if nums[l] <= target:
                if nums[l] == target:
                    return l
                elif nums[l + 1] > target:
                    return l + 1

            if nums[r] >= target:
                if nums[r] == target or nums[r - 1] < target:
                    return r
            m = l + (r - l) // 2
            if nums[m] < target:
                l = m
            else:
                r = m


s = Solution()
r = s.searchInsert([1, 3, 5, 6], 5)
print(r, r == 2)

r = s.searchInsert([1, 3, 5, 6], 2)
print(r, r == 1)

r = s.searchInsert([1, 3, 5, 6], 7)
print(r, r == 4)

r = s.searchInsert([1], 1)
print(r, r == 0)
