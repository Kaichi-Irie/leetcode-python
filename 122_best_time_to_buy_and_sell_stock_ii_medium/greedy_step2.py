#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#


# @lc code=start
import math


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Find the maximum profit using a greedy approach
        # We find monotonic increasing subsequences from the prices
        # and sum the differences between the last element of the previous
        # This can be achieved by summing up the positive difference for each day
        n_days = len(prices)
        if n_days <= 1:
            return 0

        total_profit = 0
        for i in range(1, n_days):
            price_diff = prices[i] - prices[i - 1]
            if price_diff > 0:
                total_profit += price_diff

        return total_profit


# @lc code=end
