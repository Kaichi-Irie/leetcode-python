# 問題へのリンク
[322. Coin Change - LeetCode](https://leetcode.com/problems/coin-change/description/)

# 言語
Python

# 問題の概要
与えられた種類のコインを使って、特定の金額を作るために必要な最小のコイン枚数を求める問題である。作ることが不可能な場合は `-1` を返す。これは動的計画法（DP）の典型的な問題である。

# 自分の解法

## Step1: 初期実装
まず、何も見ずに自力で解いた最初のバージョンである。

```python
CANNOT_CHANGE = -1
INFINITY = 10**5


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # min_num_coins[n] = min{min_num_coins[n-c]+1 | for c = coins[0],...,coins[-1] such that n-c>=0}
        if not coins:
            return CANNOT_CHANGE
        min_num_coins = [INFINITY] * (amount + 1)
        min_num_coins[0] = 0

        for amount_ in range(1, amount + 1):
            min_amount_sofar = INFINITY
            for coin in coins:
                if amount_ < coin:
                    continue
                min_amount_sofar = min(
                    min_amount_sofar, min_num_coins[amount_ - coin] + 1
                )

            min_num_coins[amount_] = min(min_amount_sofar, INFINITY)

        if min_num_coins[amount] == INFINITY:
            return CANNOT_CHANGE
        else:
            return min_num_coins[amount]
```

### 実装のポイント
- **アルゴリズム**: ボトムアップの動的計画法（DP）を採用した。`dp[i]` を「金額 `i` を作るための最小コイン枚数」と定義し、`dp[0]` から順番にテーブルを埋めていく。
- **状態遷移式**: `dp[i] = min(dp[i], dp[i - coin] + 1)` という基本的なDPの状態遷移式を実装している。
- **無限大の表現**: 到達不可能な状態を示す値として、問題の制約から十分大きいと考えられる `10**5` を `INFINITY` として使用した。
- **冗長なロジック**: 内側のループで `min_amount_sofar` という一時変数を使い、ループの最後で `min()` を再度呼び出すなど、コードに冗長な部分が見られる。

- **時間計算量**: `O(S*N)` (S: `amount`, N: `len(coins)`)
- **空間計算量**: `O(S)`

## Step2:

```python
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # Number of coins does not exceed amount because minimum value of a coin is one, which means this INFINITY value works as an upper bound of number of coins.
        INFINITY = amount + 1
        min_num_coins = [INFINITY] * (amount + 1)
        min_num_coins[0] = 0
        for current_amount in range(1, amount + 1):
            for coin in coins:
                previous_amount = current_amount - coin
                if previous_amount < 0:
                    continue
                min_num_coins[current_amount] = min(
                    min_num_coins[current_amount],
                    min_num_coins[previous_amount] + 1,
                )

        if min_num_coins[amount] == INFINITY:
            return -1
        return min_num_coins[amount]
```

### Step1からの変更点
- **無限大の表現の改善**: `INFINITY` の値を、ハードコードされたマジックナンバー `10**5` から `amount + 1` に変更した。コインの最小値は `1` であるため、コインの枚数が `amount` を超えることはありえない。したがって、`amount + 1` は「到達不可能」を示すセンチネル値として機能し、問題の制約が変わってもコードの堅牢性が保たれる。
- **ロジックの簡素化**: 一時変数 `min_amount_sofar` を廃止し、DPテーブル `min_num_coins` を直接更新するようにした。これにより、内側のループが状態遷移式そのものになり、コードがより直感的になった。
- **変数名の改善**: `amount_` を `current_amount` に変更し、可読性を向上させた。

### 発見
- `float("inf")`はIEEE 754で定義された特別な値で、無限大を表す。そのため、近似値でもなく、誤差もない。しかし、配列の各要素の更新の処理で、floatとintの比較や演算が入ることを避ける（type checkが入ると型安全でないとwarningが出る）ため、今回は`amount + 1`を代わりに使用した。
- `min(Iterable arg)`関数には`default`という引数があり、これは`arg`が空のときに返す値を指定できる。これを指定せずに空リストを`min`に渡すと`ValueError`になる。

## Step3
```python
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # Number of coins does not exceed amount because minimum value of a coin is one, which means this INFINITY value works as an upper bound of number of coins.
        INFINITY = amount + 1

        min_num_coins = [INFINITY] * (amount + 1)
        min_num_coins[0] = 0

        for current_amount in range(1, amount + 1):
            for coin in coins:
                if current_amount < coin:
                    continue
                min_num_coins[current_amount] = min(
                    min_num_coins[current_amount], min_num_coins[current_amount - coin] + 1
                )

        if min_num_coins[amount] == INFINITY:
            return -1
        return min_num_coins[amount]
```

`previous_amount = current_amount - coin`と置いた方が可読性が上がる気がする。



# 別解・模範解答

## トップダウンDP (メモ化再帰)
`step2_topdown_dp.py` として実装。

```python
from functools import cache


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # Number of coins does not exceed amount because minimum value of a coin is one, which means this INFINITY value works as an upper bound of number of coins.
        INFINITY = amount + 1

        @cache
        def min_coin_change(amount: int) -> int:
            assert amount >= 0
            if amount == 0:
                return 0
            min_num_coins = INFINITY
            for coin in coins:
                if amount < coin:
                    continue
                min_num_coins = min(min_num_coins, min_coin_change(amount - coin) + 1)
            return min_num_coins

        min_num_coins = min_coin_change(amount)
        # cannot change
        if min_num_coins == INFINITY:
            return -1
        return min_num_coins
```

### 実装のポイント
- 再帰関数と `functools.cache` デコレータ（メモ化）を用いてトップダウンで問題を解く。
- `amount` から開始し、必要なサブプロブレム（より小さい金額）だけを計算する。
- ボトムアップに比べ、コードが問題の再帰的な構造を素直に表現しているため、思考プロセスが自然である。

- **時間計算量**: `O(S*N)`
- **空間計算量**: `O(S)` (再帰の深さ + メモ化テーブル)

## BFS (幅優先探索)

```python
from collections import deque


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        Solves the coin change problem by treating it as a shortest path problem on a graph. Each amount is a node, and each coin represents an edge.

        This implementation uses Breadth-First Search (BFS) to find the shortest path from the `amount` node to the `0` node. The length of this path corresponds to the minimum number of coins required.
        """
        queue = deque([(amount, 0)])
        visited: set[int] = {amount}
        while queue:
            current_amount, num_coins = queue.popleft()
            if current_amount == 0:
                return num_coins
            for coin in coins:
                if current_amount < coin:
                    continue
                next_amount = current_amount - coin
                if next_amount not in visited:
                    visited.add(next_amount)
                    queue.append((next_amount, num_coins + 1))
        # cannot change
        return -1
```

### 実装のポイント
- この問題を、状態遷移のグラフにおける最短経路問題として捉える解法である。
- 各金額をグラフのノードと見なし、`amount` から `0` までの最短経路（＝最小枚数）をBFSで探索する。
- `queue` には `(現在の金額, これまでのコイン枚数)` のタプルを格納する。
- `visited` セットを用いて、同じ金額を再度探索する無駄を省く。

- **時間計算量**: `O(S*N)` (最悪ケースでは全状態を訪れる)
- **空間計算量**: `O(S)` (queueとvisitedセットのサイズ)

# 想定されるフォローアップ質問

## CS 基礎
**「もしコインの種類が非常に多く、金額 `amount` が比較的小さい場合、ボトムアップとトップダウンのDPでは、どちらのアプローチが有利になるか？その逆はどうか？」**

- **コイン多・金額小の場合**: **トップダウン**が有利である。
  - **理由**: トップダウンは目標金額から必要な部分問題だけを計算する。多くのコインが金額 `amount` より大きく、計算に寄与しない場合、それらのコインを使った計算パスは探索されず、無駄な計算を大幅に削減できる。一方、ボトムアップは全ての金額について全てのコインを試すため、無駄な計算が多くなる。
- **コイン少・金額大の場合**: **ボトムアップ**が有利である。
  - **理由**: 金額が非常に大きいと、トップダウンは再帰呼び出しの深度が深くなり、Pythonの再帰深度上限に達して `RecursionError` を引き起こすリスクがある。また、関数呼び出しのオーバーヘッドも無視できなくなる。ボトムアップは単純なループであるため、これらの問題がなく安定して動作する。

## システム設計
**「この `coinChange` 関数を、実際のPOSシステムのお釣り計算エンジンとして組み込むとします。この関数は1日に何百万回も呼び出されます。パフォーマンスを最大化するために、どのようなシステムレベルの最適化を検討しますか？」**

1.  **キャッシュ戦略**:
    - **リクエストレベルのキャッシュ**: 同じ `(coins, amount)` の組み合わせでの呼び出し結果をキャッシュする。`functools.lru_cache` のようなインメモリキャッシュが有効である。DPの計算途中の結果もキャッシュされるため効果的。
    - **永続キャッシュ**: アプリケーションを再起動しても結果が消えないよう、RedisやMemcachedのような外部キャッシュストアに結果を保存する。これにより、複数のサーバーインスタンス間でもキャッシュを共有できる。
    - **キャッシュの無効化**: 使用されるコインの種類（`coins`）が変更された場合（例: 新しい記念硬貨の追加）、キャッシュ全体を無効化（パージ）する必要がある。

2.  **前処理と定数倍最適化**:
    - **DPテーブルの前計算**: もしコインの種類が固定（例: 日本円）であれば、アプリケーション起動時に、頻繁に使われる一定範囲の金額（例: 1円から1万円まで）に対するDPテーブルを予め計算し、メモリ上に保持しておく。これにより、多くのリクエストはO(1)のテーブル参照で完了する。
    - **コインのソート**: DPの計算前に `coins` 配列をソートしておく。そして、内側のループで `current_amount < coin` となったら、それ以降のコインは明らかに大きすぎるため、ループを `break` で早期に打ち切る。これにより、平均的な実行時間を改善できる。



##
# 次に解く問題の予告
- [Binary Tree Level Order Traversal - LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- [Unique Paths - LeetCode](https://leetcode.com/problems/unique-paths/description/)
