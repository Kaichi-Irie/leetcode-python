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

テストケース
```python
root = [2,1,3] -> True
root = [1] -> True
root = [2, 1, 3] -> True
root = [2, null, 3] -> True
root = [2, 1, null] -> True
root = [1, 1, 2] -> False
root = [2, 1, 2] -> False
```
- 「各subtreeがBSTか」、「subtreeの最小値・最大値」を再帰的に取得し、rootの値と比較することでBSTかどうかを判定している。
- が、関数として自然でない上に、コードが冗長になってしまっている。
- step2以降の`lower`/`upper`を用いた方法の方がシンプルに実装できる。

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

- 時間計算量：`O(n)`
- 空間計算量：`O(n)`



# 想定されるフォローアップ質問

## CS 基礎

## システム設計

## その他

# 次に解く問題の予告
