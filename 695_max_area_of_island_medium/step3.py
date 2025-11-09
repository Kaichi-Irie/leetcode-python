#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        num_rows = len(grid)
        num_columns = len(grid[0])
        ISLAND = 1

        def is_island(cell: tuple[int, int]) -> bool:
            row, column = cell
            return (
                0 <= row < num_rows
                and 0 <= column < num_columns
                and grid[row][column] == ISLAND
            )

        def calculate_area_bfs(
            initial_island: tuple[int, int], visited_cells: set
        ) -> int:
            if not is_island(initial_island):
                return 0

            cells_to_visit = deque([initial_island])
            visited_cells.add(initial_island)
            area = 1
            DIRECTIONS = ((0, 1), (0, -1), (-1, 0), (1, 0))
            while cells_to_visit:
                row, column = cells_to_visit.popleft()
                for dr, dc in DIRECTIONS:
                    neighbor = (row + dr, column + dc)
                    if is_island(neighbor) and neighbor not in visited_cells:
                        visited_cells.add(neighbor)
                        cells_to_visit.append(neighbor)
                        area += 1
            return area

        max_area = 0
        visited_cells = set()
        for row in range(num_rows):
            for column in range(num_columns):
                cell = (row, column)
                if is_island(cell) and cell not in visited_cells:
                    area = calculate_area_bfs(cell, visited_cells)
                    max_area = max(max_area, area)
        return max_area


# @lc code=end
