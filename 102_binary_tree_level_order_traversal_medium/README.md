# 問題へのリンク
[Binary Tree Level Order Traversal - LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal/description/)


# 言語
Python

# 問題の概要
与えられた二分木の各レベルにおけるノードの値をリストとして返す問題。


# 自分の解法

## step1

```python
from collections import defaultdict


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        level_to_values: dict[int, list[int]] = defaultdict(list)

        def search(node: TreeNode | None, level: int) -> None:
            if not node:
                return
            level_to_values[level].append(node.val)
            if node.left:
                search(node.left, level + 1)
            if node.right:
                search(node.right, level + 1)

        search(root, 0)
        num_levels = len(level_to_values)
        level_to_values_list = [[] for _ in range(num_levels)]
        for level, values in level_to_values.items():
            level_to_values_list[level] = values
        return level_to_values_list
```

- ロジックはBFSと同じくらい明確
- 実運用を見据えると、以下のような使い分けになりそう。よりスケーラブルなのはBFSか？
    - 木が平衡二分木に近く、メモリ効率を重視する場合→DFS
    - 木がすべてメモリに載らない場合→BFS
    - 木が非常に偏っている場合→BFS
    - 各レベルごとに取得したい場合→BFS

ノードの数を`n`、木の最大高さを`H`とすると、
- 時間計算量：`O(n)`
- 空間計算量：`O(H)`


## step2 DFS

```python
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        level_to_values: list[list[int]] = []

        def traverse_tree(node: TreeNode | None, level: int) -> None:
            if not node:
                return
            while len(level_to_values) <= level:
                level_to_values.append([])
            level_to_values[level].append(node.val)
            if node.left:
                traverse_tree(node.left, level + 1)
            if node.right:
                traverse_tree(node.right, level + 1)

        traverse_tree(root, 0)
        return level_to_values
```

- Step1では辞書を使っていたが、はじめからリストを用いることで、最後にリストに変換する手間を省いた
- step1、step2ではpre-order traversalを用いた。
    - post-orderでも動くが、pre-orderの方が「訪れた順に値がリストに入る」という要件に対して、より自然に思える

計算量：ステップ1に同じ


## step3
```python
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        nodes = [root]
        level_order_node_vals = []
        while nodes:
            node_vals = []
            next_level_nodes = []
            for node in nodes:
                node_vals.append(node.val)
                if node.left:
                    next_level_nodes.append(node.left)
                if node.right:
                    next_level_nodes.append(node.right)
            level_order_node_vals.append(node_vals)
            nodes = next_level_nodes
        return level_order_node_vals
```

## step4 (FB)


# 別解・模範解答
## BFS（レベルばらばら）
```python
from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        node_queue = deque([(root, 0)])  # (node,level)
        level_to_values: list[list[int]] = []
        while node_queue:
            node, level = node_queue.popleft()
            while len(level_to_values) <= level:
                level_to_values.append([])
            level_to_values[level].append(node.val)
            if node.left:
                node_queue.append((node.left, level + 1))
            if node.right:
                node_queue.append((node.right, level + 1))

        return level_to_values
```

## BFS（レベルごと）

- 可読性が高く、実運用上も自然（各レベルごとにデータを取得したい場面には使いやすい）

```python
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        level_to_values = []
        nodes = [root]
        while nodes:
            this_level_values = []
            child_nodes = []
            for node in nodes:
                if not node:
                    continue
                this_level_values.append(node.val)
                if node.left:
                    child_nodes.append(node.left)
                if node.right:
                    child_nodes.append(node.right)
            level_to_values.append(this_level_values)
            nodes = child_nodes
        return level_to_values
```


ノードの数を`n`、木の最大幅を`W`とすると、
- 時間計算量：`O(n)`
- 空間計算量：`O(W)`


# 想定されるフォローアップ質問

## CS 基礎
Q.「あなたが実装した反復的なBFSアプローチの空間計算量は、木のどのような特性に依存しますか？また、深さ優先探索（DFS）を用いた再帰的なアプローチと比較した場合、どのような形状の木でBFSがより多くのメモリを消費し、逆にどのような形状の木でDFSがより多くのメモリを消費するか、具体例を挙げて説明してください。」
A.
- BFSアプローチの空間計算量は木の最大幅に依存する。
    - もし木が完全二分木なら、キューの最大サイズは`n//2=O(n)`になる。
- DFSアプローチの空間計算量は木の最大深さに依存する。
    - 例えば、非常に偏った木（例えば、すべてのノードが右の子ノードのみを持つ場合）では、DFSの再帰スタックが`O(n)`になる可能性がある。逆に、完全二分木ではDFSの最大深さは`O(log n)`であり、BFSの方が多くのメモリを消費する。

## システム設計
Q. 「このlevelOrder関数を、非常に巨大な木（例えば、数百万ノード）を扱うサービスの一部として利用するシナリオを考えます。クライアント（例: Webフロントエンド）は、一度に全レベルを表示するのではなく、'次のレベルを取得'ボタンでレベルを1つずつ要求します。このような要求に応じて効率的にデータを返すには、現在の実装をどのように変更しますか？メモリ効率を特に重視してください。」
- 全てのレベルに対する値のリストをメモリに置くのでは無く、Pythonのジェネレーターを使って、必要なレベルの値を逐次的に生成するように変更する。
    - メモリに保持する必要があるのは各レベルの値のリストのみで、全レベルのリストを保持する必要は無いため、メモリ効率が向上する。
- もし木のデータがデータベースに保存されている場合、各レベルのノードをクエリで取得するようにする。
    - 例えば、各ノードが親ノードのIDを持つようなテーブル構造を考える。
    - クライアントが特定のレベルを要求した際、そのレベルのノードをデータベースから直接クエリで取得する。
    - これにより、メモリ使用量を最小限に抑えつつ、必要なデータのみを効率的に取得できる。

## その他

# 次に解く問題の予告
- [Meeting Rooms II - LeetCode](https://leetcode.com/problems/meeting-rooms-ii/)
- [Linked List Cycle II - LeetCode](https://leetcode.com/problems/linked-list-cycle-ii/)
- [Split BST - LeetCode](https://leetcode.com/problems/split-bst/)
