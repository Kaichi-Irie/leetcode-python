# 問題へのリンク
[50. Pow(x, n)](https://leetcode.com/problems/powx-n/)

# 言語
Python

# 問題の概要
浮動小数点数 `x` と整数 `n` が与えられたとき、`x` の `n` 乗を計算する。

# 自分の解法

## step1
まず、繰り返し二乗法を再帰関数を用いて実装した。

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Compute x to the power of n based on these four facts;
        - x^(-n) = (1/x)^n (n>0)
        - x^0 = 1
        - x^1 = x
        - if n = 2*q + r, then x^(n) = (x^q)^2 * (x)^r

        """
        if n < 0:
            return self.myPow(1 / x, -n)
        if n == 0:
            return 1.0
        if n == 1:
            return x
        quotient, remainder = n // 2, n % 2

        return self.myPow(x, quotient) ** 2 * self.myPow(x, remainder)
```

- `n`が偶数の場合は `x^n = (x^(n/2))^2`、奇数の場合は `x^n = x * (x^((n-1)/2))^2` となる性質を利用した再帰的な解法である。
- `n`を2で割っていくため、再帰の深さは`log(n)`となる。
- 時間計算量：`O(log(n))`。各`n`に対する計算は一度しか行われないためである。
    - `remainder`は常に0または1であり、この計算はたかだか定数時間であるため、全体の計算量に大きな影響はない。（メモ化は不要）
    - （個人的には）`n%2`が1か0かで場合分けするよりも、`remainder`をそのまま`myPow`に渡す方がわかりやすいと感じた。数学的に必ず`n=2*q+r`なら`x^n=(x^q)^2 * (x)^r`となるため
- 空間計算量：`O(log(n))`。再帰呼び出しのスタックに`log(n)`の空間が必要である。

### 発見
- べき乗演算子`**`の挙動について、`func(x) ** 2` のような式は `func(x)` を1回だけ評価することを確認した。

## step2
step1の再帰実装では空間計算量が`O(log(n))`であったため、これを`O(1)`に改善すべく、反復処理による実装に変更した。

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Compute x to the power of n using doubling.
        Example: x=2.0, n = 10
        n = 2^3 + 2^1
        x^n = x^(2^3) * x^(2^1)

        Each x^(2^k) can be computed recursively;
        x^(2^(k+1)) = x^(2*2^k) = x^(2^k) * x^(2^k)
        """
        if n == 0:
            return 1.0
        if x == 0.0:
            return 0.0
        if n < 0:
            # x^(-n) = (1/x)^n = 1/(x^n) (n>0)
            return 1 / self.myPow(x, -n)
        x_to_power_of_two = x  # x^(2^0)
        x_to_n = 1.0  # x^n
        while n > 0:
            if n % 2 == 1:
                x_to_n *= x_to_power_of_two

            # x^(2^(k+1)) = x^(2*2^k) = x^(2^k) * x^(2^k)
            x_to_power_of_two = x_to_power_of_two * x_to_power_of_two
            n //= 2
        return x_to_n
```

- このアプローチは、`n`を2進数として捉えるものである。例えば `n=10` (2進数で`1010`) の場合、`x^10 = x^8 * x^2` となる。
- ループ内で`n`を右にシフト（`n //= 2`）しながら、最下位ビットが1かどうか（`n % 2 == 1`）を確認する。
- ビットが1であれば、その位置に対応する`x`のべき乗（`x`, `x^2`, `x^4`, `x^8`, ...）を結果に乗算していく。
- `x`のべき乗は、ループごとに自身を2乗することで効率的に計算される。
- 時間計算量：`O(log(n))`。ループ回数が`n`のビット数に比例するためである。
- 空間計算量：`O(1)`。変数の使用量が`n`の大きさに依存しないためである。

## step3
```python

```

## step4 (FB)
```python

```

# 別解・模範解答
```python

```

# 次に解く問題の予告
- [Coin Change - LeetCode](https://leetcode.com/problems/coin-change/)
- [Binary Tree Level Order Traversal - LeetCode](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- [Unique Paths - LeetCode](https://leetcode.com/problems/unique-paths/description/)
