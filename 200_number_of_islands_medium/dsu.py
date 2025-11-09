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
        num_cols = len(grid[0])

        def is_land(row: int, column: int) -> bool:
            return (
                0 <= row < num_rows
                and 0 <= column < num_cols
                and grid[row][column] == "1"
            )

        parents: dict[tuple[int, int], tuple[int, int]] = {}
        ranks: dict[tuple[int, int], int] = {}

        for row in range(num_rows):
            for col in range(num_cols):
                if is_land(row, col):
                    parents[(row, col)] = (row, col)
                    ranks[(row, col)] = 0

        def find(node):
            root = node
            while root != parents[root]:
                root = parents[root]
            while node != root:
                parent = parents[node]
                parents[node] = root
                node = parent
            return root

        def unite(node1, node2):
            root1 = find(node1)
            root2 = find(node2)
            if ranks[root1] > ranks[root2]:
                parents[root2] = root1
            elif ranks[root2] > ranks[root1]:
                parents[root1] = root2
            else:
                parents[root2] = root1
                ranks[root1] += 1


        directions = ((1, 0), (-1, 0),  (0, 1), (0, -1))
        for row in range(num_rows):
            for col in range(num_cols):
                if not is_land(row, col):
                    continue
                for dr, dc in directions:
                    neighbor = (row + dr, col + dc)
                    if is_land(neighbor[0], neighbor[1]):
                        unite((row, col), neighbor)

        roots = {find(cell) for cell in parents}
        return len(roots)
# @lc code=end
