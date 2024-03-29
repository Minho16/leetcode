class Solution:
    def maxSatisfaction(self, satisfaction: list[int]) -> int:
        prefix_sum = 0
        cur_sum = 0
        max_sum = 0

        for num in sorted(satisfaction, reverse=True):
            prefix_sum += num
            cur_sum += prefix_sum
            max_sum = max(max_sum, cur_sum)

        return max_sum
