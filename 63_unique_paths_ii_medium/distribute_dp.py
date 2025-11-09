#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        OBSTACLE = 1
        if not obstacleGrid:
            return 0

        OBSTACLE = 1
        num_rows = len(obstacleGrid)
        num_columns = len(obstacleGrid[0])
        num_paths = [[0] * num_columns for _ in range(num_rows)]

        if obstacleGrid[0][0] == OBSTACLE:
            return 0
        num_paths[0][0] = 1
        for row in range(num_rows):
            for column in range(num_columns):
                if obstacleGrid[row][column] == OBSTACLE:
                    num_paths[row][column] = 0
                if row < num_rows - 1:
                    num_paths[row + 1][column] += num_paths[row][column]
                if column < num_columns - 1:
                    num_paths[row][column + 1] += num_paths[row][column]
        return num_paths[-1][-1]


# @lc code=end
