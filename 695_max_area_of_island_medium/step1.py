#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        # search for all cells. If island cell is found, then search for all connected island cells recursively. To reduce time complexity, we use visited cells.

        WATER = 0
        ISLAND = 1

        height = len(grid)
        if height <= 0:
            raise ValueError("grid height must be more than 0")
        width = len(grid[0])

        def is_valid(i: int, j: int) -> bool:
            return 0 <= i < height and 0 <= j < width

        visited_cells: set[tuple[int, int]] = set()
        max_area = 0
        for i in range(height):
            for j in range(width):
                if (i, j) in visited_cells:
                    continue
                cell = grid[i][j]
                if cell == WATER:
                    continue

                visited_cells.add((i, j))
                area = 1

                connected_islands = [(i, j)]
                while connected_islands:
                    i, j = connected_islands.pop()
                    for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                        i_neighbor, j_neighbor = i + di, j + dj
                        if (
                            not is_valid(i_neighbor, j_neighbor)
                            or (i_neighbor, j_neighbor) in visited_cells
                        ):
                            continue

                        neighbor_cell = grid[i_neighbor][j_neighbor]
                        if neighbor_cell == ISLAND:
                            visited_cells.add((i_neighbor, j_neighbor))
                            connected_islands.append((i_neighbor, j_neighbor))
                            area += 1

                max_area = max(area, max_area)
        return max_area


# @lc code=end
