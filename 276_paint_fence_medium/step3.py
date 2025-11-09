#
# @lc app=leetcode id=276 lang=python3
#
# [276] Paint Fence
#


# @lc code=start
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return k
        previous_total_ways = k
        total_ways = k * k
        for _ in range(3, n + 1):
            total_ways, previous_total_ways = (k - 1) * (
                total_ways + previous_total_ways
            ), total_ways

        return total_ways


# @lc code=end
