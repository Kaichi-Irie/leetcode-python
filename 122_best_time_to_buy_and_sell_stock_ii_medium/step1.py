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
        max_profit_with_stock_at_day = [0] * n_days
        max_profit_without_stock_at_day = [0] * n_days

        max_profit_with_stock_at_day[0] = -prices[0]
        max_profit_without_stock_at_day[0] = 0
        for day in range(1, n_days):
            # hold or buy this day
            max_profit_with_stock_at_day[day] = max(
                max_profit_with_stock_at_day[day - 1],
                max_profit_without_stock_at_day[day - 1] - prices[day],
            )
            # do nothing or sell this day
            max_profit_without_stock_at_day[day] = max(
                max_profit_without_stock_at_day[day - 1],
                max_profit_with_stock_at_day[day - 1] + prices[day],
            )

        max_profit = max_profit_without_stock_at_day[n_days - 1]
        return max_profit


# @lc code=end
