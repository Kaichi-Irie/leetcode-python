# 問題へのリンク
[Best Time to Buy and Sell Stock II - LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/)

# 言語
Python

# 問題の概要
各日の株価が与えられて、何度でも株を売買できるとき、得られる利益の最大値を求める問題。ただし、一度に保有できる株は1つまでという制約がある。
# 自分の解法
（状態を持つ）DPを用いて各日までの利益の最大値を保持、更新して求める。

## step1
次の二つの値を各日で管理する。
1. `max_profit_without_stock_at_day` - その日の終わりに株を持っていない状態での最大利益
2. `max_profit_with_stock_at_day` - その日の終わりに株を持っている状態での最大利益

これらを各日の株価に基づいて更新していく。


- 時間計算量：O(n)
- 空間計算量：O(n)
### レビューより
- `p_current`は`current_price`とすべき
- `n_days`は`num_days`とすべき
    -  c.f. [styleguide \| Style guides for Google-originated open-source projects](https://google.github.io/styleguide/pyguide.html#316-naming)

## step2

- 実際に必要なのは、最終日の値のみで、各日の更新も前日の値からのみ行われるため、配列ではなく変数で管理することにして、空間計算量をO(1)に削減した
- `max_profit_without_stock_at_day`と`max_profit_with_stock_at_day`の変数名が長いので、`holding`と`not_holding`に変更した
- コメントを充実させ、英語も改善した


# 別解・模範解答
## step1
貪欲法による解法。
単調増加する部分列をすべて見つけて、その部分列の差分を利益として合計する。
買った株を同日に同価格で売ることができるという前提から、この部分列の長さは1でもよい。
次のアルゴリズムで最大利益を求める。
1. 初日は株を買う
2. その後、株価が上昇している間は持ち続ける
3. 株価が下落したら、下落の直前で売る

株価の配列を`prices`とすると、左端を`math.inf`、右端を`-math.inf`とすることで、実装が簡潔にできる。

- 時間計算量：O(n)
- 空間計算量：O(n)

## step2
そもそも、各日の当日と前日との株価を比較して、その差が正であればその差を利益として加算するだけでよいことに気づいた。
実装が断然簡潔になり、パフォーマンスも向上した。
`prices`の拡張を考えるのは、実装上わかりにくいので、こちらの方が好ましい。

- 時間計算量：O(n)
- 空間計算量：O(1)


# 次に解く問題の予告
- Permutations
