#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
# inplace solution
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        WATER = 0
        ISLAND = 1
        num_rows = len(grid)
        num_columns = len(grid[0])

        def is_valid(row: int, column: int) -> bool:
            return 0 <= row < num_rows and 0 <= column < num_columns

        def is_island(row: int, column: int) -> bool:
            return is_valid(row, column) and grid[row][column] == ISLAND

        def _calculate_area_of_connected_islands_inplace(
            row: int, column: int, grid: list[list[int]]
        ):
            if grid[row][column] == WATER:
                return 0
            # make the cell water, which means "the cell is visited".
            grid[row][column] = WATER
            cells_to_visit = deque(
                [
                    (row, column),
                ]
            )
            area = 1
            while cells_to_visit:
                row, column = cells_to_visit.pop()
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    row_neighbor, column_neighbor = row + dr, column + dc
                    if is_island(row_neighbor, column_neighbor):
                        # make the cell water, which means "the cell is visited".
                        grid[row_neighbor][column_neighbor] = WATER
                        cells_to_visit.append((row_neighbor, column_neighbor))
                        area += 1
            return area

        max_area = 0
        for row in range(num_rows):
            for column in range(num_columns):
                if is_island(row, column):
                    area = _calculate_area_of_connected_islands_inplace(
                        row, column, grid
                    )
                    max_area = max(max_area, area)
        return max_area


# @lc code=end
