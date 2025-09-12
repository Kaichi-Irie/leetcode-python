# 問題へのリンク


# 言語
Python

# 問題の概要


# 自分の解法

## step1

```python
class Solution:
    def zigzagLevelOrder(self, root) -> list[list[int]]:
        if not root:
            return []
        LEFT_TO_RIGHT = 1
        RIGHT_TO_LEFT = -1
        direction = LEFT_TO_RIGHT
        nodes = [root]
        zigzag_level_nodes = []
        while nodes:
            node_vals = []
            next_level_nodes = []
            while nodes:
                node = nodes.pop()
                node_vals.append(node.val)
                if direction == LEFT_TO_RIGHT:
                    if node.left:
                        next_level_nodes.append(node.left)
                    if node.right:
                        next_level_nodes.append(node.right)
                else:
                    if node.right:
                        next_level_nodes.append(node.right)
                    if node.left:
                        next_level_nodes.append(node.left)

            zigzag_level_nodes.append(node_vals)
            nodes = next_level_nodes
            direction *= -1
        return zigzag_level_nodes
```

- 時間計算量：`O(n)`
- 空間計算量：`O(n)`

## step2

```python
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        zigzag_level_nodes = []
        nodes = deque([(root, 0)])
        while nodes:
            next_nodes = deque([])
            while nodes:
                node, level = nodes.popleft()
                while len(zigzag_level_nodes) <= level:
                    zigzag_level_nodes.append(deque([]))

                # left to right
                if level % 2 == 0:
                    zigzag_level_nodes[level].append(node.val)
                # right to left
                else:
                    zigzag_level_nodes[level].appendleft(node.val)

                if node.left:
                    next_nodes.append((node.left, level + 1))
                if node.right:
                    next_nodes.append((node.right, level + 1))

            nodes = next_nodes

        return [list(deq) for deq in zigzag_level_nodes]
```


- BFSで各レベルごとに走査していくのはstep1と同じ。だが、走査するのは左から順に行い、値の追加だけzigzagになるようにする。

## step3


レベルごとに走査を行う方法（`step3_1.py`）。直感的だが、ネストが深くなる。
リストを再代入していくのもあまり良くないかも。

```python
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        zigzag_node_vals: list[deque[int]] = [deque([])]  # deque
        nodes = [root]
        next_level_nodes = []
        level = 0

        while nodes:
            for node in nodes:
                if node is None:
                    continue
                next_level_nodes.append(node.left)
                next_level_nodes.append(node.right)
                # left to right; FIFO
                if level % 2 == 0:
                    zigzag_node_vals[level].append(node.val)
                else:  # right to left; LIFO
                    zigzag_node_vals[level].appendleft(node.val)
            nodes = next_level_nodes
            next_level_nodes = []
            level += 1
            zigzag_node_vals.append(deque([]))
        return [list(deq) for deq in zigzag_node_vals]
```
- 点を走査する順番自体を工夫するのか、あるいは値の追加の仕方を工夫するのか。
    - 今回なら、点は普通に左から順に走査していき、値の追加の仕方をzigzagにするのが楽
- 初期値の設定、各ループでの更新のタイミングは統一するのが良い
    - 例えば、`next_level_nodes`の初期化をループの外で行い、ループの最後で空にするようにした
    - `level`の初期化をループの外で行い、ループの最後でインクリメントするようにした



`nodes`をキューで管理して、ネストを1つ浅くする方法（`step3_2.py`）
```python
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        zigzag_node_vals: list[deque[int]] = []  # deque
        nodes_queue = deque([(root, 0)])
        while nodes_queue:
            node, level = nodes_queue.popleft()
            if node is None:
                continue
            while len(zigzag_node_vals) <= level:
                zigzag_node_vals.append(deque([]))
            if level % 2 == 0:  # from left to right; FIFO
                zigzag_node_vals[level].append(node.val)
            else:  # from right to left; LIFO
                zigzag_node_vals[level].appendleft(node.val)

            nodes_queue.append((node.left, level + 1))
            nodes_queue.append((node.right, level + 1))
        return [list(deq) for deq in zigzag_node_vals]
```

## step4 (FB)



# 別解・模範解答
## DFS

```python
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        nodes_by_level = []

        def traverse(node: TreeNode, level: int):
            while len(nodes_by_level) <= level:
                nodes_by_level.append(deque([]))
            if level % 2 == 0:
                nodes_by_level[level].append(node.val)
            else:
                nodes_by_level[level].appendleft(node.val)

            if node.left:
                traverse(node.left, level + 1)
            if node.right:
                traverse(node.right, level + 1)

        traverse(root, 0)

        return [list(d) for d in nodes_by_level]
```

- 再帰関数を用いてグラフを走査していく。
- 各レベルごとのノードのリストを`deque`として保持して、
    - `level` が奇数のときは走査した順、つまりFIFOの順にノードを追加していく。
    - `level` が偶数のときは逆順、つまりLIFOの順にノードを追加していく。
- 最後に`deque`をリストに変換して返す。


- 時間計算量：`O(n)`
- 空間計算量：`O(n)`

# 想定されるフォローアップ質問

## CS 基礎

## システム設計

## その他

# 次に解く問題の予告
- Permutations
