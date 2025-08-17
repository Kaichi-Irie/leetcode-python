#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
from functools import cache


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        INFINITY = amount + 1

        @cache
        def min_coin_change(amount: int) -> int:
            assert amount >= 0
            if amount == 0:
                return 0
            min_num_coins = INFINITY
            for coin in coins:
                if amount < coin:
                    continue
                min_num_coins = min(min_num_coins, min_coin_change(amount - coin) + 1)
            return min_num_coins

        min_num_coins = min_coin_change(amount)
        # cannot change
        if min_num_coins == INFINITY:
            return -1
        return min_num_coins


# @lc code=end
