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
            found = False

            while not found:

                mid_point = (end-start) // 2

                if target == nums[mid_point]:
                    found = True
                    return mid_point
                else:
                    if target > nums[mid_point]:
                        start = mid_point - 1
                    elif target < nums[mid_point]:
                        end = mid_point + 1


s = Solution()

nums = [1,3,5,6] 
target = 2

print(s.searchInsert(nums, target))



