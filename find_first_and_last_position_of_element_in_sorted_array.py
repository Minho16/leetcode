class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # handle edge cases
        if nums == []:
            return [-1, -1]
        elif nums[0] > target or nums[-1] < target:
            return [-1, -1]

        left, right = 0, len(nums) - 1
        found = False
        found_idx = 0

        # check if target is found within nums through binary search
        while left <= right and not found:
            mid = (right + left) // 2
            if nums[mid] == target:
                found = True
                found_idx = mid
            elif nums[left] == target:
                found = True
                found_idx = left
            elif nums[right] == target:
                found = True
                found_idx = right
            elif target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1

        if not found:
            return [-1, -1]
        else:
            left_idx, right_idx = found_idx, found_idx
            found_left, found_right = False, False
            while left_idx > 0 and not found_left:
                if nums[left_idx - 1] == target:
                    left_idx -= 1
                else:
                    found_left = True

            while right_idx < len(nums) - 1 and not found_right:
                if nums[right_idx + 1] == target:
                    right_idx += 1
                else:
                    found_right = True

            return [left_idx, right_idx]


s = Solution()
# print(s.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
print(s.searchRange(nums=[1], target=1))
