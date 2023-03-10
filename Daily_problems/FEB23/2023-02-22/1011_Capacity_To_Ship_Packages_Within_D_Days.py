class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        '''
            1. Packages MUST be shipped in the order given 
            2. Return the least weight capacity of the ship to move all packages during the given days
            
            Binary search: with max(weights) and sum(weights) 

            Make a helper function to check if it is possible to carry out with mid value
            if so --> higher values are eliminated --> right = mid
            if not --> lower values also cannot be --> left = mid + 1
        
        '''
        left, right = max(weights), sum(weights)        
        while left < right:
            mid = (left + right) // 2
            is_possible = self.check_if_possible_with_mid(mid, weights, days)
            if is_possible:
                right = mid 
            else:
                left = mid + 1
        return left
    


    def check_if_possible_with_mid(self, mid, weights, days):
        counted_days, current_weight = 1, 0
        is_possible = True
        for weight in weights:
            if current_weight + weight <= mid:
                current_weight += weight
            else:
                counted_days += 1
                current_weight = weight

            if counted_days > days:
                is_possible = False
                break
        
        return is_possible


s = Solution()
print(s.shipWithinDays(weights=[1,2,3,4,5,6,7,8,9,10], days=5))
