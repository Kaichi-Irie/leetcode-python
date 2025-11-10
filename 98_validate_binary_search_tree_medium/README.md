# 問題へのリンク
[98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)

# 言語
Python


# 自分の解法

## step1

```python
class Solution:
    def isValidBST(self, root: TreeNode|None) -> bool:
        if root is None:
            return True
        def find_validity_and_minmax(root: TreeNode) -> tuple[bool, int, int]:
            min_val = max_val = root.val
            if root.left is not None:
                is_left_valid, min_val, left_max = find_validity_and_minmax(root.left)
                if not is_left_valid or left_max >= root.val:
                    return False, 0, 0
            if root.right is not None:
                is_right_valid, right_min, max_val = find_validity_and_minmax(root.right)
                if not is_right_valid or root.val >= right_min:
                    return False, 0, 0
            return True, min_val, max_val
        is_valid, _, _ = find_validity_and_minmax(root)
        return is_valid
```

`n`をノード数とすると、
- 時間計算量：`O(n)`
- 空間計算量：`O(n)`
    - もっと厳密には木の高さを`h`とすると`O(h)`。ただし、最悪の場合`h = n`。
        - 再帰呼び出しのスタックが`h`深くなるため。
    - 平衡木の場合は`O(log n)`。

テストケース
- 標準的なBSTケース：`root = [2,1,3]` -> `True`
- 標準的なBSTでないケース：`root = [5,1,4,null,null,3,6]` -> `False`
- 空の木：`root = []` -> `True`
- 単一ノード：`root = [1]` -> `True`
- 右に偏った木：`root = [2, null, 3]` -> `True`
- 左に偏った木：`root = [2, 1, null]` -> `True`
- 境界ケース：`root = [1, 1, 2]` -> `False`、`root = [2, 1, 2]` -> `False`

木をテキストとして書く方法
```
  1
 / \
2   3
     \
      4
```


- 「各subtreeがBSTか」、「subtreeの最小値・最大値」を再帰的に取得し、rootの値と比較することでBSTかどうかを判定している。
    - が、関数として自然でない上に、コードが冗長になってしまっている。
    - これは考え方としては、左右のsubtreeをgivenとして、中央にrootを置いたらそれはBSTか、という形で考えている。
    - 別の考え方は、rootから順にノードを置いていく。rootをgivenとして、左（右）のsubtreeのノードを配置していく時には、「root.valより小さい（大きい）」という制約が課されるという考え方。
- step2以降の`lower`/`upper`を用いた方法の方がシンプルに実装できる。


二分木の走査方法としては、以下の3つがある。
- Inorder (left -> root -> right)
- Preorder (root -> left -> right)
- Postorder (left -> right -> root)

## step2

```python
import math

class Solution:
    def isValidBST(self, root: TreeNode|None) -> bool:
        def is_valid(root, lower, upper):
            if not root:
                return True
            if root.val <= lower or root.val >= upper:
                return False
            return is_valid(root.left, lower, root.val) and is_valid(root.right, root.val, upper)

        return is_valid(root, -math.inf, math.inf)
```

- 「rootが、左のsubtreeの最大値より大きく、右のsubtreeの最小値より小さい」という条件を、「左のsubtreeのノードが全てroot.valより小さい、右のsubtreeのノードが全てroot.valより大きい」と言い換えれば、よりシンプルに実装できる。

## step3

## step4 (FB)



# 別解・模範解答
## 反復的な解法

rootから始めて、左右に進む際に、`lower`/`upper`の制約を更新していく。
ノードをpushした時点で、そのノードに対する制約（`lower`/`upper`）は確定するので、ノードを取り出す順序はなんでも良い（スタックでもキューでもなんでも良い）。

`iterative_lifo.py`

```python
import math

class Solution:
    def isValidBST(self, root: TreeNode|None) -> bool:
        frontiers = [(root, -math.inf, math.inf)]
        while frontiers:
            node, lower, upper = frontiers.pop()
            if node is None:
                continue
            if lower >= node.val or upper <= node.val:
                return False
            frontiers.append((node.left, lower, node.val))
            frontiers.append((node.right, node.val, upper))
        return True
```


`iterative_fifo.py`
```python
import math
from collections import deque

class Solution:
    def isValidBST(self, root: TreeNode|None) -> bool:
        frontiers = deque([(root, -math.inf, math.inf)])
        while frontiers:
            node, lower, upper = frontiers.popleft()
            if node is None:
                continue
            if not (lower < node.val < upper):
                return False
            frontiers.append((node.left, lower, node.val))
            frontiers.append((node.right, node.val, upper))
        return True
```

- 時間計算量：`O(n)`
- 空間計算量：`O(n)`
    - 今度は、木が非常に偏っている場合は`O(1)`になるが、平衡木の場合は`O(n)`になる。
        - スタック/キューにノードが最大で`n/2`個入る可能性があるため。


# 想定されるフォローアップ質問

- Q. 再帰的な解法と反復的な解法の違い、使い分けは？
    - A. 再帰的な解法はコードがシンプルになる一方で、再帰の深さの分だけメモリを消費する。この問題では、木が偏っている場合には、再帰的な解法はスタックオーバーフローのリスクがあるため、反復的な解法が好まれる場合がある。一方、木が平衡に保たれている場合、反復的な解法よりも再帰的な解法の方が空間計算量が小さくなる。

# 次に解く問題の予告
- [Word Ladder - LeetCode](https://leetcode.com/problems/word-ladder/description/)
- [Top K Frequent Elements - LeetCode](https://leetcode.com/problems/top-k-frequent-elements/description/)
