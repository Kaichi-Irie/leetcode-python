# 問題へのリンク
[Evaluate Division - LeetCode](https://leetcode.com/problems/evaluate-division/description/)

# 言語
Python

# 問題の概要
与えられた式のリストとその値をもとに、変数間の比率を求める問題。例えば、`a / b = 2.0`、`b / c = 3.0` という関係式が与えられ、`a / c` の値を求めるクエリが与えられた場合、`a / c = 2.0 * 3.0 = 6.0` と計算できる。

# 自分の解法

DFSを用いた解法。
```python
from collections import defaultdict

CANNOT_DETERMINED = -1.0


class Solution:
    def calcEquation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:
        """
        First, we create a graph, and create two nodes and an edge for given an equation [A,B], value v (=A/B) like shown below
        A - v -> B
        A <- 1/v - B

        To answer each query, we check if start and target node are connected using DFS and return their ratio if connected.
        """
        graph = defaultdict(dict)
        for (a, b), val in zip(equations, values):
            graph[a][b] = val
            graph[b][a] = 1 / val

        def dfs(start: str, target: str, visited: set[str]) -> float:
            if start not in graph or target not in graph:
                return CANNOT_DETERMINED

            visited.add(start)
            if start == target:
                return 1.0
            for neighbor, ratio in graph[start].items():
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                ratio_neighbor_to_d = dfs(neighbor, target, visited)
                if ratio_neighbor_to_d != CANNOT_DETERMINED:
                    return ratio * ratio_neighbor_to_d

            return CANNOT_DETERMINED

        answers = []
        for c, d in queries:
            visited = set()
            answers.append(dfs(c, d, visited))
        return answers
```

与えられた関係式を重み付き有向グラフとして表現し、各クエリに対して、DFSを用いて、始点から終点までのパスを探索し、パス上の重みを掛け合わせて比率を求める。

関係式の数を`n`、クエリの数を`Q`とすると、グラフの頂点数は最大`2n`、エッジ数は最大`2n`となる。
各DFS探索は、最悪の場合、全ての頂点を訪れる可能性があるため、各クエリに対する時間計算量は`O(n)`となる。
DFSでは再帰的に探索を行うため、空間計算量は`O(n)`となる。
- 時間計算量：`O(Qn)`
- 空間計算量：`O(n)`

## step2

## step3

#### Union-Find
1. 28min
2. 20min
どうしてもUnion-Find木のデータ構造実装→各クエリ処理となって実装が重いので10minを超えてしまう。
あと、すでに登録された要素の`add`、登録されていない要素の`find`などの処理を行うところで時間がかかる。そもそも実装を見直すべきかもしれない。

#### DFS
1. 12.5min

# 別解・模範解答
Union-Find（またはDisjoint Set Union, DSU）を用いた解法。時間計算量の観点からは、こちらの方が効率的。だが、実装が複雑になる。
各変数をノードとするUnion-Find木を構築し、与えられた関係式（`equation`）に基づいて木を結合していく。
結合した際には、子ノードと親ノードとの比率（`ratio_to_parent`）も記録する。
高速化のため、path compressionとunion by rankを用いる。

実用的には、本問は為替レートの計算に類似しており、そのようなケースでは大量のクエリを裁く必要があるため、Union-Findの方が適している。


- 時間計算量：`O(n+Qα(n))`
  - `n`は与えられた関係式の数、`Q`はクエリの数。
  - Union-Findの各操作（結合、検索）は平均的に`O(α(n))`であり、ここで`α`はアッカーマン関数の逆関数で、ほぼ定数時間と見なせる。
- 空間計算量：`O(n)`

# 次に解く問題の予告
- [Meeting Rooms - LeetCode](https://leetcode.com/problems/meeting-rooms/)
- [Largest Component Size by Common Factor - LeetCode](https://leetcode.com/problems/largest-component-size-by-common-factor/description/)
- [Longest Consecutive Sequence - LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/description/)
