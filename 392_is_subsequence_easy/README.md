# 問題へのリンク
[Is Subsequence - LeetCode](https://leetcode.com/problems/is-subsequence/description/)


# 言語
Python

# 問題の概要
二つの文字列 `s` と `t` が与えられたとき、`s` が `t` の部分列であるかどうかを判定する問題です。部分列とは、元の文字列からいくつかの文字を削除しても順序を保ったまま残すことができる文字列のことです。

> Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
>
> フォローアップ: `s` が非常に多く、例えば `s1, s2, ..., sk` のように `k >= 10^9` の場合、どのようにコードを変更しますか？



# 自分の解法
two pointersを使って、`s`と`t`の文字を順に比較していきます。`s`の文字が`t`の文字と一致した場合、`s`のポインタを進めます。`s`のポインタが最後まで進んだ場合、`s`は`t`の部分列であると判断します。

- 時間計算量：`O(len(s) + len(t))`
- 空間計算量：`O(1)`


### フォローアップ
フォローアップのケースでは、`s`が非常に多い場合、各`si`に対して`t`を走査するのは非効率的です。この場合、`t`の各文字のインデックスを事前に記録しておき、二分探索を用いて`si`の各文字が`t`に存在するかどうかを効率的に確認する方法が考えられます。

これにより時間計算量が`O(len(t) * (len(s1) + len(s2) + ... + len(sk)))`から、`O(len(t) + log(len(t)) * (len(s1) + len(s2) + ... + len(sk)))`に改善されます。
そうはいっても、`k>= 10^9`のケースでは、メモリや時間の制約が厳しいと思われます。`t`の前処理さえ済ませておけば、各`si`に対して並列処理を行えて、より効率的に処理できますが、アルゴリズムの問題の範囲を超えてしまうかもしれません。


## step2
- `rob_houses_linear`をprivateな関数`_rob_houses_linear`に変更しました
- 変数の更新の際に使う変数`tmp`を`prev_tmp`に変更しました
    - `tmp`という変数が一般に良くないというのはわかりつつも、このような一時的に値を保持して数行以内で使われるような変数ではむしろわかりやすいのでは無いかと思っています。



# 次に解く問題の予告
- [ ] [Evaluate Division - LeetCode](https://leetcode.com/problems/evaluate-division/description/)
- [ ] [Subsets - LeetCode](https://leetcode.com/problems/subsets/)
