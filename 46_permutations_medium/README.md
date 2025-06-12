# 問題へのリンク

[Permutations - LeetCode](https://leetcode.com/problems/permutations/)
# 言語
Python

# 問題の概要
与えられた整数のリスト`nums`のすべての順列を生成する問題。順列は、元のリストの要素をすべて使用して、順序を変えた新しいリストを作成すること。ただし、`nums`の要素はすべて異なる。

# 自分の解法
リストを`head`と`tail`に分け、`tail`の順列を再帰的に求め、`head`を`tail`の各順列の各位置に挿入して新しい順列を生成する。
要素`elem`とリスト`nums`を入力として、`elem`を`nums`のすべての位置に挿入して新しいリストを生成するヘルパー関数`all_insertions`を定義した。

- 時間計算量：O(n!*n^2)
- 空間計算量：O(n!*n)

## step2

## step3

# 別解・模範解答
バックトラッキングを用いて、順列を生成する。

- 時間計算量：?
- 空間計算量：?

# 次に解く問題の予告
- [Subsets - LeetCode](https://leetcode.com/problems/subsets/)
- [Group Anagrams - LeetCode](https://leetcode.com/problems/group-anagrams/)
