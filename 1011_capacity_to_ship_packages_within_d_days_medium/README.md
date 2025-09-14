# 問題へのリンク
[Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)

# 言語
Python


# 自分の解法

## step1

```python
class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        if not weights:
            return 0

        def can_ship_within_days(days: int, capacity: int) -> bool:
            cargo_weight = 0
            days_required = 1
            for weight in weights:
                if weight > capacity:
                    return False
                if cargo_weight + weight > capacity:
                    cargo_weight = 0
                    days_required += 1
                cargo_weight += weight
            return days_required <= days

        # 0 < capacity <= sum weights
        left = 0
        right = sum(weights)
        while right - left > 1:
            mid = (right + left) // 2
            if can_ship_within_days(days, mid):
                right = mid
            else:
                left = mid
        return right
```

- 単調性あるところに二分探索あり。
- `(left, right]`の範囲で二分探索するパターン。
- `can_ship_within_days`関数内で`weight > capacity`のチェックをしているが、はじめは抜けていた上、なかなか気づきづらい。
    - `left`の初期値を`0`にしていたが、`max(weights)`などにすればこのチェックは不要になる。その場合、二分探索も変わる。
    - そうはいっても、そもそも`if max(weights) > capacity: return False`とすべき。
    - 例えば`weights = [100,]`のとき、can_ship_within_days(2, 50)は`False`を返すべきだが、上記のコードでは`True`を返してしまう。これは2日に分ければ大きな荷物も運べるということになってしまうため。
- `cargo_weight`は複数の荷物をまとめた重さを表す変数としているが、`current_weight`の方がわかりやすいと思った
- `can_ship_within_days`という名前の関数で`days`が引数にないのは違和感があるので、`days`を引数にした。が、`can_ship`にリネームして`days`をキャプチャする形にしたほうが自然だと思った。

`weights`の要素数を`N`、`weights`の要素の和を`S`とすると、
- 時間計算量：`O(N log(S))`
- 空間計算量：`O(N)`

## step2

```python
class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        if not weights:
            return 0

        def can_ship(capacity: int) -> bool:
            current_weight = 0
            days_required = 1
            for weight in weights:
                if current_weight + weight > capacity:
                    current_weight = 0
                    days_required += 1
                current_weight += weight
            return days_required <= days

        # max weight <= capacity <= sum weights
        left = max(weights) - 1
        right = sum(weights)
        while right - left > 1:
            mid = (right + left) // 2
            if can_ship(mid):
                right = mid
            else:
                left = mid
        return right
```
- `can_ship_within_days`関数を`can_ship`にリネーム


## step3
```python
class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        # for given capacity, we can check if we can ship all the packages with it
        def can_ship(capacity: int) -> bool:
            if max(weights) > capacity:
                return False

            current_weight = 0
            days_required = 1
            for weight in weights:
                current_weight += weight
                if current_weight > capacity:
                    current_weight = weight
                    days_required += 1
            return days_required <= days

        left = 0
        right = sum(weights)
        while right - left > 1:
            mid = (right + left) // 2
            if can_ship(mid):
                right = mid
            else:
                left = mid

        return right
```

## step4 (FB)



# 別解・模範解答
`bisect`モジュールを使う方法

```python
import bisect


class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def can_ship(capacity: int) -> bool:
            if max(weights) > capacity:
                return False
            current_weight = 0
            days_required = 1
            for weight in weights:
                current_weight += weight
                if current_weight > capacity:
                    days_required += 1
                    current_weight = weight
            return days_required <= days

        return bisect.bisect_left(range(sum(weights) + 1), True, key=can_ship)
```

- 二分探索を自分で書く前に、まずは`bisect`モジュールを使って通るかを見るのが良い。
- `bisect`モジュールでは`key`引数が使えるので、`can_ship`関数をそのまま渡せる。
- ソート済みのリストを用意する必要があるが、`range`で用意できる。`bool`の配列ではソートすると`False`が先に来るので、`True`が初めて出現するインデックスを求めることになる。


# 次に解く問題の予告
- [Unique Paths II](https://leetcode.com/problems/unique-paths-ii/)
- [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
