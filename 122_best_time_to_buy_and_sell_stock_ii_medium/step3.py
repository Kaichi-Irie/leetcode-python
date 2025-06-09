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
        n_days = len(prices)
        holding = -prices[0]
        not_holding = 0
        for today in range(1, n_days):
            prev_holding = holding
            holding = max(holding, not_holding - prices[today])
            not_holding = max(not_holding, prev_holding + prices[today])
        return not_holding


# @lc code=end
