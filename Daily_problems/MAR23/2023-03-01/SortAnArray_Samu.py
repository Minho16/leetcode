from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(nums):
            if len(nums) < 2:
                return nums
            elif len(nums) == 2:
                if nums[0] <= nums[1]:
                    return nums
                else:
                    return [nums[1], nums[0]]
            n = len(nums)
            l = quicksort(nums[0 : n // 2])
            r = quicksort(nums[n // 2 :])
            s = []
            i = 0
            j = 0
            while i < len(l) or j < len(r):
                if i < len(l) and j < len(r):
                    if l[i] <= r[j]:
                        s.append(l[i])
                        i += 1
                    else:
                        s.append(r[j])
                        j += 1
                elif i < len(l):
                    s.append(l[i])
                    i += 1
                elif j < len(r):
                    s.append(r[j])
                    j += 1
            return s

        r = quicksort(nums)
        return r


s = Solution()
r = s.sortArray([8, 7, 6, 5, 3, 2, 1])
