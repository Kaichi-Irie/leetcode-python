#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start

CANNOT_CHANGE = -1
INFINITY = 10**5


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # min_num_coins[n] = min{min_num_coins[n-c]+1 | for c = coins[0],...,coins[-1] such that n-c>=0}
        if not coins:
            return CANNOT_CHANGE
        min_num_coins = [INFINITY] * (amount + 1)
        min_num_coins[0] = 0

        for amount_ in range(1, amount + 1):
            min_amount_sofar = INFINITY
            for coin in coins:
                if amount_ < coin:
                    continue
                min_amount_sofar = min(
                    min_amount_sofar, min_num_coins[amount_ - coin] + 1
                )

            min_num_coins[amount_] = min(min_amount_sofar, INFINITY)

        if min_num_coins[amount] == INFINITY:
            return CANNOT_CHANGE
        else:
            return min_num_coins[amount]


# @lc code=end
