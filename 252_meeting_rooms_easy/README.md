# 問題へのリンク
[Meeting Rooms - LeetCode](https://leetcode.com/problems/meeting-rooms/)

# 言語
Python

# 問題の概要

ある人が複数の会議に出席できるかを判定する問題である。

* 各会議は時間帯 `[starti, endi]` で表される。
* 入力は、こうした会議の時間帯のリスト `intervals` で与えられる。
* **すべての会議に出席するには、会議同士が重ならない必要がある。**

#### 例1:

```
入力: [[0,30],[5,10],[15,20]]
出力: false（0〜30と5〜10が重なるため）
```

#### 例2:

```
入力: [[7,10],[2,4]]
出力: true（会議が重ならないため）
```

#### 制約:

* 会議数は 0〜10,000 件
* 各会議の時間帯は `[starti, endi]`（開始 < 終了、かつ0以上1,000,000以下）


# 自分の解法
`intervals` の時間帯を開始時間でソートし、隣接する会議の終了時間と開始時間を比較する方法。ひとつでも重なっている会議があれば、`False` を返す。
- 時間計算量：`O(nlogn)`
- 空間計算量：`O(1)`

## step2

- `start`, `end` の変数名を `start_time`, `end_time` に変更して、より明確にした。

# 別解・模範解答
`intervals` からすべての時間帯のペアを取り出し、そのペアが重なるかどうかを確認する方法。

- 時間計算量：`O(n^2)`（すべてのペアを確認するため）
- 空間計算量：`O(1)`

# 次に解く問題の予告
- [Largest Component Size by Common Factor - LeetCode](https://leetcode.com/problems/largest-component-size-by-common-factor/description/)
- [Longest Consecutive Sequence - LeetCode](https://leetcode.com/problems/longest-consecutive-sequence/description/)
