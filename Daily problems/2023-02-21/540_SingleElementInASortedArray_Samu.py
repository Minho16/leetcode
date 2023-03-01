from typing import List
class Solution:
    # Binary search solution. (Runtime: 168 ms (92.86%) | Memory: 23.8 MB (14.27%))
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while r > l:
            m = l+(r-l)//2          
            if nums[m] != nums[m+1] and nums[m] != nums[m-1]:
                return nums[m]
            elif nums[m] == nums[m-1]:
                m += 1

            if (r-m-1)%2 == 0:
                r = m-1
            else:
                l = m

        return nums[l]      


s = Solution()
r = s.singleNonDuplicate([1,1,2,3,3,4,4,8,8])
print(r, r==2)

r = s.singleNonDuplicate([3,3,7,7,10,11,11])
print(r, r==10)

r = s.singleNonDuplicate([3,3,7,10,10,11,11])
print(r, r==7)
