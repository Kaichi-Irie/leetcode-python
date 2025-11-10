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
        num_rows = len(grid)
        num_columns = len(grid[0])
        num_islands = 0
        visited_lands = set()

        def is_land(row: int, column: int) -> bool:
            return (
                0 <= row < num_rows
                and 0 <= column < num_columns
                and grid[row][column] == "1"
            )

        # traverse connected lands by DFS
        directions = ((1, 0), (-1, 0),  (0, 1), (0, -1))
        def traverse_connected_lands(row, column):
            # if inplace: grid[row][column] = "0"
            visited_lands.add((row, column))
            for dr, dc in directions:
                neighbor_row = row + dr
                neighbor_column = column + dc
                if (neighbor_row, neighbor_column) in visited_lands:
                    continue
                if not is_land(neighbor_row, neighbor_column):
                    continue
                traverse_connected_lands(neighbor_row, neighbor_column)

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
