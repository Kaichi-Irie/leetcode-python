#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if not obstacleGrid:
            return 0
        OBSTACLE = 1
        num_rows = len(obstacleGrid)
        num_columns = len(obstacleGrid[0])
        num_paths_in_row = [0] * num_columns
        num_paths_in_row[0] = 1
        for row in range(num_rows):
            for column in range(num_columns):
                if obstacleGrid[row][column] == OBSTACLE:
                    num_paths_in_row[column] = 0
                    continue
                if column > 0:
                    num_paths_in_row[column] += num_paths_in_row[column - 1]

        return num_paths_in_row[-1]


# @lc code=end
