from typing import List
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total = 0
        current_l = 0
        for n in nums:
            if n == 0:
                current_l += 1
            elif current_l != 0:
                total += current_l*(current_l+1)/2
                current_l = 0
        if current_l != 0:
            total += current_l*(current_l+1)/2
            current_l = 0
        return total
