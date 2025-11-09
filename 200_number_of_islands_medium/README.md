# 問題へのリンク
[200. Number of Islands](https://leetcode.com/problems/number-of-islands/)

# 言語
Python

## step1
DFS を用いる解法。
```python
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
```

DFSは、スタックの分だけの空間を使う上、Pythonでは再起呼び出し回数の制限がデフォルトでは1000と小さいので、パフォーマンス上はBFSを用いる方が望ましい。が、DFSの方がコードがシンプルになる場合が多い。
- 時間計算量：`O(n*m)`
- 空間計算量：`O(n*m)`

## step2

```python
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
```

- gridをinplaceに書き換えてOKならば、`seen_lands.add((row, column))` を`grid[row][column] = "0"` に変更することで、`seen_lands`の代わりに元のグリッドを利用でき、空間計算量を`O(1)`に削減できる。

## step3

## step4 (FB)



# 別解・模範解答
## BFS を用いる解法

`bfs.py`
```python
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
```

## Disjoint Set Union (Union-Find) を用いる解法

`dsu.py`
```python

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
```

- 時間計算量：`O(n*m*α(k))` （αはアッカーマン関数の逆関数、kはunion/findの呼び出し回数）
- 空間計算量：`O(n*m)`
- `mydsu.py` は DSU をクラスとして実装した例。`num_disjoint_sets` を逐次管理することで、最後にルートの集合を数える計算を省略できる。

# 想定されるフォローアップ質問
- Q. もしこのグリッドが非常に巨大で、例えば数テラバイトあり、メモリに一度に収まらない場合はどうしますか？
    - A. グリッドが2行分ずつメモリに収まると仮定します。各行でDSUと島の数を逐一計算し、前の行と現在の行で接続されている島をマージしていきます。これにより、メモリ使用量を大幅に削減しつつ、正確な島の数を計算できます。


# 次に解く問題の予告
- [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
- [Word Ladder](https://leetcode.com/problems/word-ladder/description/)
- [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/description/)
