#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Find the maximum profit using dynamic programming

        # At each day, we maintain 2 states:
        # - holding: maximum profit ending the day with holding stock
        # - not_holding: maximum profit ending the day with not holding stock

        if not prices:
            return 0

        n_days = len(prices)

        # At day 0, we must buy the stock if we want
        holding = -prices[0]
        not_holding = 0

        for day in range(1, n_days):
            prev_holding = holding
            # Option 1: Keep holding the stock
            # Option 2: Buy today (only possible if not holding yesterday)
            holding = max(
                holding,
                not_holding - prices[day],
            )

            # Option 1: Keep not holding any stock
            # Option 2: Sell today (only possible if holding yesterday)
            not_holding = max(
                not_holding,
                prev_holding + prices[day],
            )

        return not_holding


# @lc code=end
