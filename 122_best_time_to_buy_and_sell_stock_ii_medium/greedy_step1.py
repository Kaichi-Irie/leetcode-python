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
        n_days = len(prices)
        extended_prices = [math.inf]
        for p in prices:
            extended_prices.append(p)
        extended_prices.append(-math.inf)
        day = 1
        total_profit = 0

        while day <= n_days:
            p_current = extended_prices[day]

            p_prev = extended_prices[day - 1]
            if p_prev <= p_current:
                day += 1
                continue
            buy = p_current

            p_next = extended_prices[day + 1]
            while day <= n_days:
                p_current = extended_prices[day]
                p_next = extended_prices[day + 1]
                if p_current <= p_next:
                    day += 1
                    continue
                else:
                    # We have found a day to sell
                    break
            sell = p_current
            total_profit += sell - buy
            day += 1

        return total_profit


# @lc code=end
