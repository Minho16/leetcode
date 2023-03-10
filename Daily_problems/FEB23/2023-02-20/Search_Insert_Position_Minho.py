class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        '''
            what is the fastest way to return the number? --> binary search since a sorted array is given at the beginning
        
            What are the conditions? 
            
            FINISH BEFORE STARTING
            - the target can be > max(nums) --> nums[len(nums)]
            - the target can be < min(nums) --> nums[0]
            
            OR BINARY SEARCH 
            - the target can be one of the nums --> return the corresponding idx of the target
            - the target can be a number between two numbers of nums --> if target > nums[i] and target < nums[i+1] --> return the idx of i+1

        
        '''

        if target < nums[0]:
            return 0
        
        elif target > nums[len(nums)-1]:
            return len(nums)
        
        else: # binary search here
            start, end = 0, len(nums)-1

            while (start <= end):

                mid_point = (start + end) // 2

                if target == nums[mid_point]:
                    return mid_point
                elif nums[mid_point] > target:
                    end = mid_point - 1
                else:
                    start = mid_point + 1
            return start
