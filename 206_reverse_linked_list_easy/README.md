# 問題へのリンク
[Reverse Linked List - LeetCode](https://leetcode.com/problems/reverse-linked-list/)

# 言語
Python

# 問題の概要
与えられた連結リストを反転させる問題。

# 自分の解法

ノードを前から順にたどっていき、一つ前のノード`previous`を保持しながら、現在のノードの`next`を前のノードに向けていく。`next`を一時的に保持しておくことで、次のノードを失わないようにする。


ノードの個数を$n$として
- 時間計算量：$O(n)$
- 空間計算量：$O(1)$

## step2
- `next`という変数名はPythonの組み込み関数と被るので、`next_node`に変更。
- `previous`の初期値を`None`から始めることでより簡潔なコードに。
## step3

# 別解・模範解答
再帰的に解く方法もある。
連結リストを`head`と`tail`に分け、`tail`を反転させた後、`head`の`next`を`tail`に向ける。


- 時間計算量：$O(n)$
- 空間計算量：$O(n)$

# 次に解く問題の予告
- Permutations
- Meeting Rooms
