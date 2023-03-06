class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        count = 0
        i = 0
        while k != 0 and i < len(arr):
            count += 1
            if arr[i] != count:
                k -= 1
            else:
                i += 1
        
        if k != 0:
            count += k

        return count
    
        '''
        worse method

        all_numbers_list = [i for i in range(1, arr[-1] + k + 1)]
        diff_list = sorted(list(set(all_numbers_list) - set(arr)))

        return diff_list[k-1]

        '''