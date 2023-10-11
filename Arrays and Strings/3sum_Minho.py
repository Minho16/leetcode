class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sum_of_two_combinations = {}

        # all sums saved as KEY and lists of indexes as VALUE (time complexity: O(n^2), space: O(n))
        idx_i = 0
        while idx_i < len(nums)-1:
            idx_j = idx_i + 1
            while idx_j < len(nums):
                if idx_i != idx_j:
                    if nums[idx_i] + nums[idx_j] not in sum_of_two_combinations.keys():
                        sum_of_two_combinations[nums[idx_i] + nums[idx_j]] = [[idx_i, idx_j]]
                    else:
                        sum_of_two_combinations[nums[idx_i] + nums[idx_j]].append([idx_i, idx_j])
                idx_j += 1
            idx_i += 1

        # traverse nums again and check if the corresponding value exists as a dictionary key and if so, check if idx_k does not match with idx_i and idx_j saved as list

        answer_list = []

        for idx_k, num_k in enumerate(nums):
            if -num_k in sum_of_two_combinations.keys():
                # the key can contain many values so need to have a for loop
                for combination in sum_of_two_combinations[-num_k]: # each combination is idx_i and idx_j
                    if idx_k not in combination: # if the idx_k does not exist

                        answer_list.append([nums[combination[0]], nums[combination[1]], nums[idx_k]])

        return answer_list


s = Solution()
s.threeSum(nums=[-1, 0, 1, 2, -1, -4])
