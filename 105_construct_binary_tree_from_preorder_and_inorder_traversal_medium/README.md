# 問題へのリンク
[105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

# 言語
Python

# 自分の解法



## step1

```python
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        def constract_tree(preorder, inorder) -> TreeNode|None:
            if not preorder:
                return None
            root_val = preorder[0]
            for root_index in range(len(inorder)):
                if inorder[root_index] == root_val:
                    break

            left_inorder = inorder[:root_index]
            right_inorder = inorder[root_index+1:]
            left_vals = set(left_inorder)
            right_vals = set(right_inorder)
            left_preorder = [val for val in preorder if val in left_vals]
            right_preorder = [val for val in preorder if val in right_vals]

            root = TreeNode(val = root_val)
            root.left = constract_tree(left_preorder, left_inorder)
            root.right = constract_tree(right_preorder, right_inorder)
            return root
        return constract_tree(preorder, inorder)
```


- https://github.com/hayashi-ay/leetcode/pull/43
    - 同じ解法でも実装が簡潔で読みやすいと感じた
    - リストには`index`メソッドがあることを知らなかった
        - `list.index(value)`でリスト内で初めに見つかった`value`のインデックスを返す。なければ`ValueError`を送出する
            - なければ `-1`を返すような実装だと、エラーに気づかず動いてしまうから? 実際、エラーを返す方が明快だと感じた
    - 時間計算量は`O(n)`なので、全体の時間計算量は変わらないが、コードがすっきりする
- この解法は計算時間的には最適ではないが、理解しやすく想起しやすいので、これをまず書いてから、効率的な解法に書き換えるのがよいと思う



木を配列に変換したときの構造
- preorder: ルート -> 左部分木 -> 右部分木
- inorder: 左部分木 -> ルート -> 右部分木
- postorder: 左部分木 -> 右部分木 -> ルート
- ※各部分木も同様に再帰的にこの性質が成り立つ
- 配列の値だけでは、どのようにブロックが区分けされているか分からないため、これらのうち2つの配列が必要になる

- 時間計算量：`O(n^2)`
- 空間計算量：`O(n)`



## step2

```python
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode|None:
        self.preorder_root_index = 0
        inorder_val_to_index = {val:i for i, val in enumerate(inorder)}
        def build(left, right) -> TreeNode|None:
            if left>right:
                return None
            root_val = preorder[self.preorder_root_index]
            self.preorder_root_index += 1
            root_index = inorder_val_to_index[root_val]
            root = TreeNode(val=root_val)
            root.left = build(left,root_index-1)
            root.right = build(root_index+1, right)
            return root
        return build(0, len(inorder)-1)
```
- 模範解答の、preorderのインデックスをグローバル変数で管理して1ずつインクリメントしていく方法。`left`と`right`でinorderの範囲を指定している
- ちなみに、二分探索木は`inorder`がソート済みになるような木。
- `preorder`のインデックスをインクリメントしていくことで探索できるところの理解が難しかった
- `build(left, right)`は`inorder[left...right]`から木を構築する。これを実行し終わった後は、`inorder`の`left`から`right`までの要素がすべて使われていることになる。呼び出しの度に`preorder_root_index`をインクリメントしていくことで、`preorder`の次の要素は常に「まだ使っていない要素」の中で`preorder`において最初の要素になる。これは部分木のルートに対応する
    - leftの要素が0または1の場合を想起すれば、理解しやすいかも

- 時間計算量：`O(n)`
- 空間計算量：`O(n)`



元の自分の解法を転置インデックスと、リストのスライスを使わない方法に書き換えたもの
`my_faster_solution.py`
```python
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode|None:
        inorder_val_to_index = {val:i for i, val in enumerate(inorder)}
        def construct_tree(preorder_left, preorder_right,inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return None
            if inorder_left > inorder_right:
                return None
            root_val = preorder[preorder_left]
            root = TreeNode(val=root_val)
            root_index = inorder_val_to_index[root_val]
            left_subtree_size = root_index - inorder_left
            root.left = construct_tree(preorder_left+1, preorder_left+left_subtree_size,inorder_left, root_index-1)
            root.right = construct_tree(preorder_left+left_subtree_size+1, preorder_right, root_index+1,inorder_right)
            return root
        return construct_tree(0, len(preorder)-1, 0, len(inorder)-1)
```
- かなり複雑かつ、バグを生みやすい実装になってしまった


## step3

## step4 (FB)



# 想定されるフォローアップ質問

## CS 基礎

## システム設計

## その他

# 次に解く問題の予告
- Permutations
