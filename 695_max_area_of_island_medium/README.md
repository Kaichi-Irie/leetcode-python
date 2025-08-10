# 問題へのリンク
[Max Area of Island - LeetCode](https://leetcode.com/problems/max-area-of-island)

# 言語
Python

# 問題の概要

与えられた2次元のグリッドにおいて、1は陸地、0は水を表す。最大の島の面積を求める問題です。島は上下左右に隣接する1の集合として定義される。

# 自分の解法
各マスを走査し、1が見つかったらそのマスを起点にグラフ探索を行い、島の面積を計算します。グラフ探索では連結成分を取り出せれば十分なので、走査の順番は特に気にしません。DFSでもBFSでも何でも解けますが、いずれにせよパフォーマンスを考えて、反復法で実装します。


## step1

```python
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        # search for all cells. If island cell is found, then search for all connected island cells recursively. To reduce time complexity, we use visited cells.

        WATER = 0
        ISLAND = 1

        height = len(grid)
        if height<=0:
            raise ValueError("grid height must be more than 0")
        width = len(grid[0])

        def is_valid(i:int,j:int)->bool:
            return 0<=i<height and 0<=j<width


        visited_cells:set[tuple[int,int]] = set()
        max_area = 0
        for i in range(height):
            for j in range(width):
                if (i,j) in visited_cells:
                    continue
                cell = grid[i][j]
                if cell == WATER:
                    continue

                visited_cells.add((i,j))
                area = 1

                connected_islands = [(i,j)]
                while connected_islands:
                    i, j = connected_islands.pop()
                    for di, dj in [[0,1], [0,-1], [1,0], [-1,0]]:
                        i_neighbor, j_neighbor = i+di,j+dj
                        if not is_valid(i_neighbor, j_neighbor) or (i_neighbor, j_neighbor) in visited_cells:
                            continue

                        neighbor_cell = grid[i_neighbor][j_neighbor]
                        if neighbor_cell == ISLAND:
                            visited_cells.add((i_neighbor,j_neighbor))
                            connected_islands.append((i_neighbor, j_neighbor))
                            area += 1


                max_area = max(area,max_area)
        return max_area
```

- 時間計算量：`O(n*m)`
- 空間計算量：`O(n*m)`

## step2

```python
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

        def _calculate_area_bfs(
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
                    area = _calculate_area_bfs(cell, visited_cells)
                    max_area = max(area, max_area)
        return max_area
```

step1からの変更点
1.  責務の分離（リファクタリング）:
    *   `step1`: 島の面積を計算するロジック（`while`ループ）が、グリッド全体を走査する`for`ループの中に直接ネストされていました。これにより、`maxAreaOfIsland`関数が長大で複雑になっていました。
    *   `step2`: 島の面積を計算するロジックを、独立したヘルパー関数 `_calculate_area_bfs` として切り出しました。これにより、`maxAreaOfIsland`関数は「グリッドを走査し、新しい島を見つけたら面積計算を依頼する」という単一の責務に集中でき、コードの可読性と保守性が向上しました。

2.  探索アルゴリズムの変更:
    *   `step1`: `list`をスタックとして利用し、`pop()`で要素を取り出す深さ優先探索（DFS）もどきを反復処理で実装していました。
    *   `step2`: `collections.deque`をキューとして利用し、`popleft()`で要素を取り出す幅優先探索（BFS）を実装しています。アルゴリズムとしては何でもいい（連結成分さえ取り出せればOK）ですが、BFSの方が有名で、読み手が理解しやすいと考えました。

3.  ヘルパー関数の追加:
    *   `step1`: 座標がグリッド範囲内かを確認する`is_valid`のみでした。
    *   `step2`: `is_valid`に加え、セルが陸地かどうかを判定する`is_island`関数を追加し、条件分岐の意図をより明確にしました。

4.  エッジケースの処理:
    *   `step1`: `if height<=0:`で`ValueError`を送出していました。
    *   `step2`: `if not grid or not grid[0]:`という、よりPythonicで一般的な方法で空のグリッドをチェックし、`0`を返しています。
    *  LeetCodeの問題では制約条件が明確なので、わざわざ不要なエッジケースの処理を追加する必要はないかもしれませんが、例えばコーディング面接や実務の場では、どういう入力を想定するか、エッジケースはどう処理するかを話し合いながら決めていき、適宜エッジケースの処理を追加することが大切

5.  コードの可読性向上:
    *   `step1`: `i`, `j`というループ変数が、外側の`for`ループと内側の`while`ループで再利用されており、混乱を招く可能性がありました。
    *   `step2`: 変数名を`row`, `column`のように、より意味の分かりやすいものに変更しました。また、方向を示すリストを`DIRECTIONS`という定数として定義し、マジックナンバーを排除しました。



## step3

- 基本的にはstep2と同じですが、タプルのアンパックなどを極力減らし、シンプルになるようにしました。

```python
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
```

## step4 (FB)

# 別解・模範解答
`grid`に対してinplaceな実装をして`visited_cells`を管理すれば空間計算量は`O(1)`になりますが、それは問題の要件依存だと思いました。`step2_inplace.py`ではそのような実装をしています。

- 時間計算量：`O(n*m)`
- 空間計算量：`O(1)`

# 次に解く問題の予告
-
