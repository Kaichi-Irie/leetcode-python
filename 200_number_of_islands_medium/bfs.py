#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        num_rows = len(grid)
        num_columns = len(grid[0])
        num_islands = 0
        num_islands = 0
        visited_lands = set()

        def is_land(row: int, column: int) -> bool:
            return (
                0 <= row < num_rows
                and 0 <= column < num_columns
                and grid[row][column] == "1"
            )

        directions = ((1, 0), (-1, 0),  (0, 1), (0, -1))
        def traverse_connected_lands(initial_row, initial_column):
            frontiers = deque([])
            frontiers.appendleft((initial_row, initial_column))
            visited_lands.add((initial_row, initial_column))
            while frontiers:
                row, column = frontiers.pop()
                for dr, dc in directions:
                    neighbor_row = row + dr
                    neighbor_column = column + dc
                    if not is_land(neighbor_row, neighbor_column):
                        continue
                    if (neighbor_row, neighbor_column) in visited_lands:
                        continue

                    visited_lands.add((neighbor_row, neighbor_column))
                    frontiers.appendleft((neighbor_row, neighbor_column))

        for row in range(num_rows):
            for column in range(num_columns):
                if not is_land(row, column):
                    continue
                if (row, column) in visited_lands:
                    continue
                traverse_connected_lands(row, column)
                num_islands += 1
        return num_islands

# @lc code=end
