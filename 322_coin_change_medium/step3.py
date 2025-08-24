#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        INFINITY = amount + 1

        min_num_coins = [INFINITY] * (amount + 1)
        min_num_coins[0] = 0

        for current_amount in range(1, amount + 1):
            for coin in coins:
                if current_amount < coin:
                    continue
                min_num_coins[current_amount] = min(
                    min_num_coins[current_amount], min_num_coins[current_amount - coin] + 1
                )

        if min_num_coins[amount] == INFINITY:
            return -1
        return min_num_coins[amount]


# @lc code=end
