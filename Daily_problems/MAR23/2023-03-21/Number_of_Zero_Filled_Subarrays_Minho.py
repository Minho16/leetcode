class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        '''
            Dynamic Programming
                When range = 1 --> 0                                            1
                When range = 2 --> 0, 0, 00                                     1 + 2
                When range = 3 --> 0, 0, 0, 00, 00, 000                         1 + 2 + 3
                When range = 4 --> 0, 0, 0, 0, 00, 00, 00, 000,  000, 0000      1 + 2 + 3 + 4

                --> total combinations of range n = n + (range n-1)

            Approach:
                A. Save in a list, the length of consecutive zeros with "counter"
                B. While reading the list, sum to the total number of occurrences accoording to the DP dictionary
                C. Save the values in a dictionary where key = range length and value = possible combinations
        '''
        counter, occurrences = 0, 0
        consecutive_zeros_length = []
        dynamic_programming_values_dict = {0: 0}

        for i in nums:
            if not i:  # i == 0
                counter += 1
            else:
                # save the accumulated counter
                consecutive_zeros_length.append(counter)
                # reset the counter
                counter = 0

        # check about the edge case
        if nums[-1] == 0:
            consecutive_zeros_length.append(counter)

        # create the values of dictionary
        max_value_of_list = max(consecutive_zeros_length)
        for i in range(1, max_value_of_list + 1):
            dynamic_programming_values_dict[i] = i \
                + dynamic_programming_values_dict[i-1]

        # sum all the values by searching the dictionary
        for length in consecutive_zeros_length:
            occurrences += dynamic_programming_values_dict[length]

        return occurrences

# SOLUTION BELOW
# class Solution:
#     def zeroFilledSubarray(self, nums: list[int]) -> int:
        # ans, count = 0, 0
        # for num in nums:
        #     if num:
        #         count = 0
        #     else:
        #         count += 1
        #     ans += count

        # return ans
