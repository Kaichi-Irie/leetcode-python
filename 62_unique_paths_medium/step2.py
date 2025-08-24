#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def combination(n: int, k: int) -> int:
            assert 0 <= k <= n
            if n == k == 0:
                return 1
            numerator = 1
            denominator = 1
            for num in range(n - k + 1, n + 1):
                numerator *= num
            for num in range(1, k + 1):
                denominator *= num
            return numerator // denominator

        vertical_moves = m - 1
        horizontal_moves = n - 1
        total_moves = vertical_moves + horizontal_moves
        return combination(total_moves, vertical_moves)


# @lc code=end
