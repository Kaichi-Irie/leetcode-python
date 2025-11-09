#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        if not grid[0]:
            return 0
        num_rows = len(grid)
        num_columns = len(grid[0])
        num_islands = 0
        seen_lands = set()

        def is_land(row:int, column:int) -> bool:
            return (0 <= row < num_rows
                    and 0 <= column < num_columns
                    and grid[row][column] == "1")

        grid_diffs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        def traverse_connected_lands(row, column):
            seen_lands.add((row, column))
            for dr, dc in grid_diffs:
                neighbor_row = row + dr
                neighbor_column = column + dc
                if not is_land(neighbor_row, neighbor_column):
                    continue
                if (neighbor_row, neighbor_column) in seen_lands:
                    continue
                traverse_connected_lands(neighbor_row, neighbor_column)
            return

        # find num_islands by multistart DFS
        for row in range(num_rows):
            for column in range(num_columns):
                # skip water
                if not is_land(row, column):
                    continue
                if (row, column) in seen_lands:
                    continue
                traverse_connected_lands(row, column)
                num_islands += 1
        return num_islands

# @lc code=end
