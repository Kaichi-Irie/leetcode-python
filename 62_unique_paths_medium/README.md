# 問題へのリンク
[Unique Paths - LeetCode](https://leetcode.com/problems/unique-paths/description/)

# 言語
Python

# 問題の概要
m x n のグリッドが与えられる。左上のマスから右下のマスまで、右または下にのみ移動する場合のユニークな経路の総数を求める問題である。

# 自分の解法

この問題は、最終的に `(m-1) + (n-1)` 回の移動のうち、どの `m-1` 回を「下」への移動にするか（残りは「右」になる）を選択する組み合わせの問題として解釈できる。したがって、組み合わせの公式 `C(m+n-2, m-1)` を用いて解くことができる。

## step1
`math.comb` を利用して、組み合わせ計算を直接実装した。これは最も簡潔で効率的な解法である。

```python
import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        return math.comb(m + n - 2, m - 1)
```

- 時間計算量：`O(min(m, n))`。`math.comb`の実装に依存するが、効率的に計算される。
- 空間計算量：`O(1)`。

## step2
`math.comb` に頼らず、組み合わせを計算する関数を自前で実装した。これにより、ライブラリの内部実装への理解を深め、特定のバージョンに依存しないコードとなる。

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def combination(n: int, k: int) -> int:
            assert 0 <= k <= n
            if n == k == 0:
                return 1
            if n - k < k:
                k = n - k
            numerator = 1
            denominator = 1
            for num in range(n - k + 1, n + 1):
                numerator *= num
            for num in range(1, k + 1):
                denominator *= num
            return numerator // denominator

        moves_to_right = n - 1
        moves_to_bottom = m - 1
        total_moves = moves_to_right + moves_to_bottom
        return combination(total_moves, moves_to_bottom)
```

- 時間計算量：`O(min(m, n))`。組み合わせの計算 `C(n, k)` のループ回数は `k` に比例するため。
- 空間計算量：`O(1)`。

# 別解・模範解答

### 1. 動的計画法 (2D DP)
`dp[i][j]` を `(i, j)` に到達する経路の数と定義する。`dp[i][j] = dp[i-1][j] + dp[i][j-1]` という漸化式で解くことができる。

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num_paths = [[0] * n for _ in range(m)]
        for row in range(m):
            for column in range(n):
                if row == 0 or column == 0:
                    num_paths[row][column] = 1
                    continue
                num_paths[row][column] = num_paths[row - 1][column] + num_paths[row][column - 1]

        return num_paths[-1][-1]
```

- 時間計算量：`O(m*n)`。グリッドの全マスを一度ずつ計算するため。
- 空間計算量：`O(m*n)`。`m x n` のDPテーブルを保持するため。

### 2. 動的計画法 (1D DP)
2D DPの空間計算量を最適化したアプローチである。`i`行目の計算は`i-1`行目の情報のみに依存するため、1次元配列を使い回すことで空間を削減できる。

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        num_paths_in_row = [1] * n
        for _ in range(1, m):
            for column in range(1, n):
                num_paths_in_row[column] += num_paths_in_row[column - 1]
        return num_paths_in_row[-1]
```

- 時間計算量：`O(m*n)`。
- 空間計算量：`O(n)`。1行分の情報を保持する配列のみ使用するため。

### 3. 再帰 (メモ化)
トップダウンの動的計画法アプローチである。`@cache`デコレータ（メモ化）を使い、重複する計算を避ける。

```python
from functools import cache


class Solution:
    @cache
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
```

- 時間計算量：`O(m*n)`。メモ化により、各 `(m, n)` の組み合わせは一度しか計算されないため。
- 空間計算量：`O(m*n)`。再帰のスタックとキャッシュのための空間が必要である。

# 次に解く問題
- [Binary Tree Level Order Traversal - LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal/)
