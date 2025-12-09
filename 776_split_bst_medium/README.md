# 問題へのリンク
[776. Split BST](https://leetcode.com/problems/split-bst/)

# 言語
Python

# 問題の概要
二分探索木（BST）が与えられたとき、指定された値 `target` を基準にして、BST を 2 つのサブツリーに分割する問題。1 つのサブツリーにはすべてのノードの値が `target` 以下であり、もう 1 つのサブツリーにはすべてのノードの値が `target` より大きいノードが含まれるようにする。元の BST の構造はできるだけ保持されるようにする。親子が同じサブツリーに属する場合、その親子関係も保持される。

tagetの値によっては、ジグザグに分割されることもあり、その場合は何度もつなぎ直すことになる。そのため、上から順に探索していくと、つなぎ直しが複雑になる。再帰関数を用いて、部分木ごとに分割していくと、つなぎ直しがシンプルになる。


# 自分の解法
再帰関数

## step1

```python
class Solution:
    def splitBST(self, root: TreeNode|None, target: int) -> list[TreeNode|None]:
        if root is None:
            return [None, None]
        if root.val <= target:
            small, large = self.splitBST(root.right, target)
            root.right = small
            return [root, large]
        small, large = self.splitBST(root.left, target)
        root.left = large
        return [small, root]
```

- 再帰関数で、root以下の部分木をtargetで分割したときの2つの部分木を返すようにする。これを再帰的に呼び出していくと、最終的にroot以下の部分木をtargetで分割したときの2つの部分木が得られる。
- 初めは、つなぎ直し方に自信が持てなかった

`h`を木の高さとすると、
- 時間計算量：`O(h)`
- 空間計算量：`O(h)`




## step2

```python

```

## step3

## step4 (FB)



# 別解・模範解答

## Stackを用いたiterativeな解法

```python
class Solution:
    def splitBST(self, root: TreeNode|None, target: int) -> list[TreeNode|None]:
        stack = [] # (node, is_greater)

        # append nodes to stack
        node = root
        while node is not None:
            if node.val <= target:
                stack.append((node, False))
                node = node.right
            else:
                stack.append((node, True))
                node = node.left

        small_node = None
        large_node = None

        while stack:
            node, is_large = stack.pop()
            if is_large:
                node.left = large_node
                large_node = node
            else:
                node.right = small_node
                small_node = node

        return [small_node, large_node]
```

- 再帰関数をStackでiterativeに書き換えたもの。子から親につなぎ直していくイメージ。

`h`を木の高さとすると、
- 時間計算量：`O(h)`
- 空間計算量：`O(h)`


## Stackを用いないiterativeな解法

```python
class Solution:
    def splitBST(self, root: TreeNode|None, target: int) -> list[TreeNode|None]:
        small_dummy = TreeNode()
        large_dummy = TreeNode()

        node = root
        small_node = small_dummy
        large_node = large_dummy
        while node is not None:
            if node.val <= target:
                small_node.right = node
                small_node = node
                next_node = node.right
                node.right = None
                node = next_node
            else:
                large_node.left = node
                large_node = node
                next_node = node.left
                node.left = None
                node = next_node

        return [small_dummy.right, large_dummy.left]
```

- 親から子につなぎにいくので、いったん切り離す必要があることに気づけなかった。注意
`h`を木の高さとすると、
- 時間計算量：`O(h)`
- 空間計算量：`O(1)`

