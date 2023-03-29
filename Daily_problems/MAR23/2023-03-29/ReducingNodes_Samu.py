from typing import List
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        s = sorted(satisfaction, reverse=True)
        # If the first element is negative, all of them are negative. Return zero
        if s[0] < 0:
            return 0

        # Elems contains all the elems that are part of the max solution
        # Biggest elements have to be in the solution
        max_satisfaction = 0
        elems = 0
        for i, sat in enumerate(s):
            # Each time we add a new dish, we have to increment the coefficient of each dish --> elems variable
            elems += s[i]

            if elems < 0: # Addig dish 'i' will only decrease the max satisfaction
                return max_satisfaction
            max_satisfaction += elems

        return max_satisfaction
