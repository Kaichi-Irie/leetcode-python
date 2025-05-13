#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
from typing import List
from math import inf

# from functools import cache


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        cheapest = inf
        for price in prices:
            cheapest = min(cheapest, price)
            max_profit = max(max_profit, price - cheapest)
        return max_profit


# @lc code=end
