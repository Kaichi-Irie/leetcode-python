# 問題へのリンク

[Group Anagrams - LeetCode](https://leetcode.com/problems/group-anagrams/)

# 言語
Python


# 自分の解法
`strs`の各文字列を順番に走査し、各文字列をソートした結果をキーとして、ハッシュマップ`anagram_groups: dict[str, list[str]]`に格納する。
アナグラム同士は、同じソート結果を持つため、同じキーに格納される。

`strs`の配列の長さを`n`、各文字列の長さの最大値を`m`とする。
本問では、`0<= n <= 10^4`、`0 <= m <= 100`である。
- 時間計算量：`O(n * m log(m))`
- 空間計算量：`O(n * m)`



## step2
- ハッシュマップを`anagram_groups`と命名。
- キーを生成する処理を`generate_anagram_key`関数に切り出す。
- ハッシュマップのキーを`canonical_key`と命名。（アナグラムの正規形を表すキー、の意）

# 別解・模範解答（`char_count_key.py`）
もし、`strs`の各文字列の長さが長い場合、ソートにかかる時間が大きくなるため、キーを文字列のカウントのタプルにする方法も考えられる。
ここで、ハッシュマップのキーに使えるのは、イミュータブルなオブジェクトである必要があるため、リストではなくタプルを使う。


`strs`の配列の長さを`n`、各文字列の長さの最大値を`m`、各文字列の含む文字の種類数を`k`とすると
本問では、`k= 26`（英小文字のみ）である。
- 時間計算量：`O(n * k)`
- 空間計量：`O(n * m)`

# 次に解く問題の予告
- [Implement Trie (Prefix Tree) - LeetCode](https://leetcode.com/problems/implement-trie-prefix-tree/description/)
- [Is Subsequence - LeetCode](https://leetcode.com/problems/is-subsequence/description/)
