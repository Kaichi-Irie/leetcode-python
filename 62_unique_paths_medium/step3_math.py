#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        moves_to_bottom = m - 1
        moves_to_right = n - 1
        total_moves = moves_to_bottom + moves_to_right
        return math.comb(total_moves, moves_to_bottom)


# @lc code=end
