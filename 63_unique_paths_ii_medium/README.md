# 問題へのリンク
[63. Unique Paths II](https://leetcode.com/problems/unique-paths-ii/)

# 言語
Python

# 自分の解法

## step1

各マスを順に見ていき、上隣と左隣からの経路数を足し合わせることで、そのマスまでの経路数を求める。障害物があるマスでは経路数を0にすればOK。

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if not obstacleGrid:
            return 0

        OBSTACLE = 1
        num_rows = len(obstacleGrid)
        num_columns = len(obstacleGrid[0])
        unique_paths = [0] * num_columns

        for row in range(num_rows):
            for column in range(num_columns):
                if obstacleGrid[row][column] == OBSTACLE:
                    unique_paths[column] = 0
                    continue
                if row == 0 and column == 0:
                    unique_paths[column] = 1
                    continue
                num_paths_from_left = 0
                if column > 0:
                    num_paths_from_left += unique_paths[column - 1]
                num_paths_from_top = 0
                if row > 0:
                    num_paths_from_top += unique_paths[column]

                unique_paths[column] = num_paths_from_left + num_paths_from_top

        return unique_paths[-1]
```
- スタート地点にも障害物がある場合があり得ることを考慮し忘れて、一度WAになった。
    - `if obstacleGrid[row][column] == OBSTACLE:...`の前に`if row == 0 and column == 0:...`を置いてしまっていた。
    - このあたりは、コーディング面接ではコードを書く前に口頭で色々と条件を確認しておくと良い。

`m` を行数、`n` を列数とすると、
- 時間計算量：`O(m * n)`
- 空間計算量：`O(n)`
    - もし`m`か`n`のどちらかが非常に大きい/小さいことがあらかじめわかっている場合、`O(min(m, n))`に最適化可能
    - まずは二次元配列を使って`O(m * n)`で解き、次に一次元配列を使って`O(n)`に最適化する、というステップを踏んだ。


## step2

```python
OBSTACLE = 1


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if not obstacleGrid:
            return 0

        num_rows = len(obstacleGrid)
        num_columns = len(obstacleGrid[0])
        num_paths_in_row = [0] * num_columns

        for row in range(num_rows):
            for column in range(num_columns):
                if obstacleGrid[row][column] == OBSTACLE:
                    num_paths_in_row[column] = 0
                    continue
                if row == column == 0:
                    num_paths_in_row[column] = 1
                    continue

                num_paths_from_left = num_paths_in_row[column - 1] if column > 0 else 0
                num_paths_from_top = num_paths_in_row[column] if row > 0 else 0
                num_paths_in_row[column] = num_paths_from_left + num_paths_from_top

        return num_paths_in_row[-1]
```


- `num_paths_from_left`と`num_paths_from_top`の計算を三項演算子で簡潔に書いた。
    - `num_paths_in_row[column] if row > 0 else 0`は実は不要で、`num_paths_in_row[column]`だけで良いが、可読性を優先した。
- `if row == 0 and column == 0:`を`if row == column == 0:`と書いた。
    - この条件分岐はループ内で0を特別扱いするような感じで、あまり美しくない。
例えば、以下のようにすれば
```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if not obstacleGrid:
            return 0
        OBSTACLE = 1
        num_rows = len(obstacleGrid)
        num_columns = len(obstacleGrid[0])
        num_paths_in_row = [0] * num_columns
        num_paths_in_row[0] = 1
        for row in range(num_rows):
            for column in range(num_columns):
                if obstacleGrid[row][column] == OBSTACLE:
                    num_paths_in_row[column] = 0
                    continue
                if column > 0:
                    num_paths_in_row[column] += num_paths_in_row[column - 1]

        return num_paths_in_row[-1]
```
とすれば、`if row == 0 and column == 0:`の条件分岐は不要になってスッキリはするが、`num_paths_from_left`と`num_paths_from_top`として明示的に書く方が、アルゴリズムの意図がわかりやすいと考えた。

## step3
```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if not obstacleGrid:
            return 0
        OBSTACLE = 1
        num_rows = len(obstacleGrid)
        num_columns = len(obstacleGrid[0])
        num_paths_in_row = [0] * num_columns
        for row in range(num_rows):
            for column in range(num_columns):
                if obstacleGrid[row][column] == OBSTACLE:
                    num_paths_in_row[column] = 0
                    continue
                if row == column == 0:
                    num_paths_in_row[column] = 1
                    continue
                num_paths_from_top = num_paths_in_row[column] if row > 0 else 0
                num_paths_from_left = num_paths_in_row[column - 1] if column > 0 else 0
                num_paths_in_row[column] = num_paths_from_top + num_paths_from_left

        return num_paths_in_row[-1]
```



## step4 (FB)



# 別解・模範解答


配るDP：`distribute_dp.py`
```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        OBSTACLE = 1
        if not obstacleGrid:
            return 0

        OBSTACLE = 1
        num_rows = len(obstacleGrid)
        num_columns = len(obstacleGrid[0])
        num_paths = [[0] * num_columns for _ in range(num_rows)]

        if obstacleGrid[0][0] == OBSTACLE:
            return 0
        num_paths[0][0] = 1
        for row in range(num_rows):
            for column in range(num_columns):
                if obstacleGrid[row][column] == OBSTACLE:
                    num_paths[row][column] = 0
                if row < num_rows - 1:
                    num_paths[row + 1][column] += num_paths[row][column]
                if column < num_columns - 1:
                    num_paths[row][column + 1] += num_paths[row][column]
        return num_paths[-1][-1]
```

- 時間計算量：`O(m * n)`
- 空間計算量：`O(m * n)`

本問の場合、1次元DPで配るDPは、アルゴリズムとして不自然な気がする。

# 想定されるフォローアップ質問

- 「現在の問題では、各セルへの移動コストはすべて1（単に移動するだけ）です。ここにもし、『各セルを通過するのに特定のコストがかかり、ゴールまでに許される総コストが決まっている』という制約が加わった場合、どのようなアプローチで問題を解きますか？アルゴリズムと、その際に必要となるデータ構造について説明してください。」
    - 新しいDPの状態として、dp[i][j][k] のような3次元配列を提案する。ここで i は行、j は列、k はその時点での累積コストを表す。dp[i][j][k] には、「コスト k を使ってセル (i, j) に到達する経路の数」を格納する。状態遷移式は、dp[i][j][k + cost[i][j]] = dp[i-1][j][k] + dp[i][j-1][k] のようになる。最終的な答えは、ゴール地点 (R-1, C-1) における、許容総コスト以下のすべての k に対する dp[R-1][C-1][k] の合計になる。


# 次に解く問題の予告
- [Subarray Sum Equals K - LeetCode](https://leetcode.com/problems/subarray-sum-equals-k/description/)
- [String to Integer (atoi) - LeetCode](https://leetcode.com/problems/string-to-integer-atoi/description/)
- [Number of Islands - LeetCode](https://leetcode.com/problems/number-of-islands/description/)
