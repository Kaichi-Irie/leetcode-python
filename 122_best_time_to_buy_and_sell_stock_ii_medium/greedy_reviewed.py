#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#


# @lc code=start
import math


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        for day in range(1, len(prices)):
            diff = prices[day] - prices[day - 1]
            if diff > 0:
                max_profit += diff
        return max_profit


# @lc code=end
