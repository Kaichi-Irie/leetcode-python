#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# @lc code=start
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        WATER = "0"
        LAND = "1"
        num_rows = len(grid)
        num_cols = len(grid[0])
        num_islands = 0
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        def traverse(row, col):
            for dr, dc in directions:
                neighbor_row = row + dr
                neighbor_col = col + dc
                if not (0 <= neighbor_row < num_rows):
                    continue
                if not (0 <= neighbor_col < num_cols):
                    continue
                if grid[neighbor_row][neighbor_col] == WATER:
                    continue
                grid[neighbor_row][neighbor_col] = WATER
                traverse(neighbor_row, neighbor_col)

        for row in range(num_rows):
            for col in range(num_cols):
                if grid[row][col] == LAND:
                    traverse(row, col)
                    num_islands += 1
        return num_islands

# @lc code=end
