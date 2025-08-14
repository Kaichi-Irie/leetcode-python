#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start

from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        """
        maxAreaOfIsland searches for all cells. If island cell is found and it is not visited yet, then search for all connected islands for it.
        """
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

        def calculate_area_bfs(
            initial_island: tuple[int, int], visited_cells: set
        ) -> int:
            if not is_island(*initial_island):
                return 0
            area = 1
            cells_to_visit = deque([initial_island])
            DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0))

            while cells_to_visit:
                row, column = cells_to_visit.popleft()
                for dr, dc in DIRECTIONS:
                    neighbor = (row + dr, column + dc)
                    if is_island(*neighbor) and neighbor not in visited_cells:
                        visited_cells.add(neighbor)
                        cells_to_visit.append(neighbor)
                        area += 1
            return area

        visited_cells: set[tuple[int, int]] = set()
        max_area = 0
        for row in range(num_rows):
            for column in range(num_columns):
                cell = (row, column)
                if is_island(*cell) and cell not in visited_cells:
                    visited_cells.add(cell)
                    area = calculate_area_bfs(cell, visited_cells)
                    max_area = max(area, max_area)
        return max_area


# @lc code=end
