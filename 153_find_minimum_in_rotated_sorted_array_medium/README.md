# 問題へのリンク
[Find Minimum in Rotated Sorted Array - LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)

# 言語
Python

# 問題の概要
回転された昇順ソート配列から最小値を見つける。配列の回転とは、要素を一つずつ右にずらす操作を指す。例えば、`[3, 4, 5, 1, 2]`は`[1, 2, 3, 4, 5]`を回転させた結果である。
本問では時間計算量が`O(log(n))`であることが求められる。

# 自分の解法
二分探索を用いて、回転された配列の最小値を見つける。配列の中央の要素と端の要素を比較し、どちら側に最小値が存在するかを判断する。
元の配列を`a0<a1<a2<...<an`とすると、回転された配列は`ak+1< ak+2<...<an > a0<a1<...<ak`のような形になる。この性質を利用して、二分探索を行う。

`left`と`right`をぞれぞれ配列の左端と右端のインデックスとして初期化し、中央の要素を計算する。中央の要素が右端の要素より大きい場合、最小値は右側にあるため、`left`を`mid`に更新する。逆に、中央の要素が右端の要素以下の場合、最小値は左側または中央にあるため、`right`を`mid`に更新する。この操作を繰り返し、最終的に`right`が最小値のインデックスとなる。
二分探索では常に`nums[left] > nums[right]`が成り立つように、`left`と`right`の更新を行う。

- 時間計算量：`O(log(n))`
- 空間計算量：`O(1)`

## step2
- `L`, `R`をそれぞれ`left`, `right`に置き換える。
    - 大文字はPEP8に反する。大文字は定数に使うべき。
    - 1文字の変数名はPEP8に反する
    - `L`, `R`が市民権を得ているのはatcoderだけ


# 次に解く問題の予告
- [Evaluate Division - LeetCode](https://leetcode.com/problems/evaluate-division/description/)
- [Subsets - LeetCode](https://leetcode.com/problems/subsets/)
