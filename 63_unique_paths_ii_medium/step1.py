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
        unique_paths = [0] * num_columns

        for row in range(num_rows):
            for column in range(num_columns):
                if obstacleGrid[row][column] == OBSTACLE:
                    unique_paths[column] = 0
                    continue
                if row == 0 and column == 0:
                    unique_paths[column] = 1
                    continue
                num_paths_from_left = 0
                if column > 0:
                    num_paths_from_left += unique_paths[column - 1]
                num_paths_from_top = 0
                if row > 0:
                    num_paths_from_top += unique_paths[column]

                unique_paths[column] = num_paths_from_left + num_paths_from_top

        return unique_paths[-1]


# @lc code=end
