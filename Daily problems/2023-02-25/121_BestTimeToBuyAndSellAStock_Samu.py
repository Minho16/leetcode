class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        :type prices: List[int]
        :rtype: int
        """
        # O(n) complexity.
        # Similar solution to optimal one, use max(), min()
        max_p = 0
        min_p = prices[0]
        for i in range(len(prices)-1): 
            if prices[i+1] - min_p > max_p:
                max_p = prices[i+1] - min_p
            elif prices[i+1] < min_p:
                min_p = prices[i+1] 
        return max_p