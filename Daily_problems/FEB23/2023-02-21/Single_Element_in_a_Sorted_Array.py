class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        """
        binary search + O(1) time complexity

        Always two numbers --> check the idx where it varies

        1. Check the idx of mid is odd or even

        2. By each case, check left and right numbers and reduce the list to check

            - If mid idx is odd -->
                - if nums[mid idx-1] == nums[mid_idx] --> the single element is in the left side
                - if nums[mid idx+1] == nums[mid_idx] --> the single element is in the right side
                - if nums[mid] != nums[mid_idx+1] and nums[mid] != nums[mid_idx-1] --> case found

            - If mid idx is even -->
                - if nums[mid idx-1] == nums[mid_idx] --> the single element is in the right side
                - if nums[mid idx+1] == nums[mid_idx] --> the single element is in the left side
                - if nums[mid] != nums[mid_idx+1] and nums[mid] != nums[mid_idx-1] --> case found

        3. Handle exception cases (if len(nums) == 1) // the length cannot be 2 (NEVER)

        """

        if len(nums) == 1:
            return nums[0]

        start, end = 0, len(nums) - 1
        found = False
        answer = None

        while not found:
            mid = (start + end) // 2

            if (end - start) == 2:
                if nums[mid] == nums[mid - 1]:
                    return nums[mid + 1]
                elif nums[mid] not in [nums[mid - 1], nums[mid + 1]]:
                    return nums[mid]
                else:
                    return nums[mid - 1]

            else:
                if (mid % 2) - 1 != 0:  # mid = even
                    if (
                        nums[mid - 1] == nums[mid]
                    ):  # single element is in the right side
                        end = mid - 1
                    elif nums[mid + 1] == nums[mid]:
                        start = mid
                    elif (
                        nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]
                    ):  # case found
                        found = True
                        answer = nums[mid]
                else:  # mid = odd
                    if nums[mid - 1] == nums[mid]:  # single element is in the left side
                        start = mid
                    elif nums[mid + 1] == nums[mid]:
                        end = mid - 1
                    elif (
                        nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]
                    ):  # case found
                        found = True
                        answer = nums[mid]

        return answer


nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
s = Solution()
print(s.singleNonDuplicate(nums))
