#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
from collections import deque


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        top_left = (0, 0)
        num_paths_grid = [[0 for _ in range(n)] for _ in range(m)]
        num_paths_grid[top_left[0]][top_left[1]] = 1
        queue: deque[tuple[int, int]] = deque([top_left])
        directions = ((0, 1), (1, 0))
        visited: set[tuple[int, int]] = set([top_left])

        def is_valid(row, column) -> bool:
            return 0 <= row < m and 0 <= column < n

        while queue:
            row, column = queue.popleft()
            num_paths = num_paths_grid[row][column]
            neighbors = [(row + drow, column + dcol) for drow, dcol in directions]
            for neighbor_row, neighbor_col in neighbors:
                if not is_valid(neighbor_row, neighbor_col):
                    continue
                num_paths_grid[neighbor_row][neighbor_col] += num_paths
                if (neighbor_row, neighbor_col) in visited:
                    continue
                visited.add((neighbor_row, neighbor_col))
                queue.append((neighbor_row, neighbor_col))
        return num_paths_grid[m - 1][n - 1]


# @lc code=end
