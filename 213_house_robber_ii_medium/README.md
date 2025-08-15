# 問題へのリンク
[House Robber II - LeetCode](https://leetcode.com/problems/house-robber-ii/description/)

# 言語
Python

# 問題の概要
この問題は、円形の家のリストが与えられたときに、隣接する家を盗むことができない条件の下で、最大の金額を盗む方法を見つけることです。
家が一列に並んでいる場合の最大金額を求める問題[House Robber - LeetCode](https://leetcode.com/problems/house-robber/description/)と似ていますが、円形の配置により、最初と最後の家は隣接しています。つまり、最初の家と最後の家の両方を盗むことはできないという制約が追加されています。



# 自分の解法
以下の二つの場合に分けて考えます。円形の制約から、求める答えは以下の二つのケースのうちいずれかになります。
1. 最初の家を盗まない場合（最後の家は盗んでもよい）
2. 最後の家を盗まない場合（最初の家は盗んでもよい）

そして、それぞれのケースに対して、通常の「House Robber」の問題を動的計画法で解くことで、最大金額を求めます。動的計画法の際には、二つの変数の値だけを逐次更新していくことで、空間計算量を`O(1)`に抑えます。


- 時間計算量：`O(len(nums))`
- 空間計算量：`O(1)`

## step2
- `rob_houses_linear`をprivateな関数`_rob_houses_linear`に変更しました
- 変数の更新の際に使う変数`tmp`を`prev_tmp`に変更しました
    - `tmp`という変数が一般に良くないというのはわかりつつも、このような一時的に値を保持して数行以内で使われるような変数ではむしろわかりやすいのでは無いかと思っています。



## step3
- dpの漸化式をコメントに書きました
    - `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`
    - `dp[i]`は`i`番目の家まで考えたときの最大金額を表します。

# 次に解く問題の予告
- [ ] [Evaluate Division - LeetCode](https://leetcode.com/problems/evaluate-division/description/)
- [ ] [Subsets - LeetCode](https://leetcode.com/problems/subsets/)
