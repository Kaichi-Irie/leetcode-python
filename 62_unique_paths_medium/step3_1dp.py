#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num_paths_in_row = [0] * n
        num_paths_in_row[0] = 1
        for _ in range(m):
            for column in range(1, n):
                num_paths_in_row[column] += num_paths_in_row[column - 1]
        return num_paths_in_row[-1]


# @lc code=end
