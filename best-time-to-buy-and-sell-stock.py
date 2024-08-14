class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #sliding window, dynamic, if we come across a larger number on our right pointer, we want to snap our left pointer, otherwise keep moving right pointer

        max_profit = 0

        l, r = 0, 1

        while r < len(prices):
            max_profit = max(max_profit, prices[r] - prices[l])
            if prices[r] < prices[l]:
                l = r
            r+=1

        return max_profit

        #O(n) using dynamic sliding window technique
