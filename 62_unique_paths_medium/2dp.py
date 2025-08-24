#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num_paths = [[0] * n for _ in range(m)]
        for row in range(m):
            for column in range(n):
                if row == 0 or column == 0:
                    num_paths[row][column] = 1
                    continue
                num_paths[row][column] = num_paths[row - 1][column] + num_paths[row][column - 1]

        return num_paths[-1][-1]


# @lc code=end
