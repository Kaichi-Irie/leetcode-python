#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        profit_when_holding = -prices[0]
        profit_when_not_holding = 0
        for today in range(1, len(prices)):
            prev_holding = profit_when_holding
            profit_when_holding = max(profit_when_holding, profit_when_not_holding - prices[today])
            profit_when_not_holding = max(profit_when_not_holding, prev_holding + prices[today])
        return profit_when_not_holding


# @lc code=end
