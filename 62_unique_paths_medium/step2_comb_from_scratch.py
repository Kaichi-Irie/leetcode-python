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
            if n - k < k:
                k = n - k
            numerator = 1
            denominator = 1
            for num in range(n - k + 1, n + 1):
                numerator *= num
            for num in range(1, k + 1):
                denominator *= num
            return numerator // denominator

        moves_to_right = n - 1
        moves_to_bottom = m - 1
        total_moves = moves_to_right + moves_to_bottom
        return combination(total_moves, moves_to_bottom)


# @lc code=end
