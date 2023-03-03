
from typing import List
import heapq

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        min_v = min(nums)
        max_v = max(nums)
        dif = max_v - min_v
        
        last_min = -1
        last_max = -1
        change1 = True
        while change1:
            if max_v % 2 == 0:
                if max_v/2 != last_max and max_v/2 != last_min:
                    last_max = max_v 
                    nums[nums.index(max_v)] = max_v/2
                    max_v = max(nums)
                    last_min = min_v
                    min_v = min(nums)
                    change1 = True
                    if max_v - min_v < dif:
                        dif = max_v - min_v
                else:
                    change1 = False
 
            
            elif min_v % 2 == 1:
                if min_v*2 != last_max and min_v*2 != last_min:
                    last_min = min_v 
                    nums[nums.index(min_v)] = min_v*2
                    min_v = min(nums)
                    last_max = max_v
                    max_v = max(nums)
                    change1 = True
                    if max_v - min_v < dif:
                        dif = max_v - min_v    
                else:
                    change1 = False
            else:
                    change1 = False
        return int(dif)
            

            




s = Solution()
r = s.minimumDeviation([1,2,3,4])
print(r, r==1)

r = s.minimumDeviation([4,1,5,20,3])
print(r, r==3)

r = s.minimumDeviation([2,10,8])
print(r, r==3)

r = s.minimumDeviation([192978346,153948939,147725900,128959020,152949311,173602535,195643978,120013972,142084051,136108423,121580658,145565683,156257215,199766954,187813699,171156531,162645972,100216855,139697220,182202999,147699018,110023818,176058211,185321487,176811279,100190707,135798617,116045000,140572589,172900728,116145251,140651548,165834418,116121994,186652919,103162165,164716217,117471904,155970321,113282879,105493962,103599601,188489301,155340595,136108503,127347508,194267446])
print(r, r==92000128)

r = s.minimumDeviation([399,908,648,357,693,502,331,649,596,698])
print(r, r==315)