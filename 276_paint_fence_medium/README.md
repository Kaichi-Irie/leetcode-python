# 問題へのリンク
[Paint Fence - LeetCode](https://leetcode.com/problems/paint-fence/)

# 言語
Python

# 問題の概要
- `n` 本のフェンス(のポスト)があり、`k` 色のペンキを使って塗る
- 3 本以上の隣接するフェンスは同じ色に塗れない
- `n` 本のフェンスを塗る方法の数を求めよ

# 自分の解法: Bottom-Up DP
`n` 本のフェンスを塗る方法の数を`n`についての漸化式で求める。`k`は固定して考える。

`n` 本のフェンスを塗る方法の数を求めるために、以下のように考える。
- `n` 本目と `n-1` 本目のフェンスが同じ色でない場合
    - `n` 本目のフェンスは `k-1` 色から選べる。
    - `1` 本目から `n-1` 本目のフェンスを塗る方法の数は `count[n-1]` となる。
- `n` 本目と `n-1` 本目のフェンスが同じ色である場合、`n`, `n-1` 本目のフェンスは `k-1` 色から選べる。
    - `1` 本目から `n-2` 本目のフェンスを塗る方法の数は `count[n-2]` となる。


したがって、`count[n]` を `n` 本のフェンスを塗る方法の数とすると、
- `count[n] = (k - 1) * count[n - 1] + (k - 1) * count[n - 2]`

- `count[1] = k`, `count[2] = k * k` (`n = 2` の場合は、どの色を選んでも隣接するフェンスと同じ色にならないため)とを併せて考えると、`count[n]` が`n`回のループで求まる。

動的計画法の配列は使わず、`count[n-1]` と `count[n-2]` の値を保持する変数を用いて計算することで空間計算量を`O(1)`に抑える。

- 時間計算量：`O(n)`
- 空間計算量：`O(1)`


## step1

```python
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        # Suppose k is given.
        # Use dynamic programming
        # count[n]: number of possibilities using n posts with k different colors
        # count[1] = k, count[2] = k*k
        # count[n] = (k-1) * count[n-1] + (k-1) * count[n-2], for all n = 3, 4, ...

        previous_count = k
        count = k * k
        for _ in range(3, n + 1):
            tmp_count = count
            count = (k - 1) * count + (k - 1) * previous_count
            previous_count = tmp_count
        return count
```


## step2


- `count`という変数名は曖昧すぎたので`total_ways`などに変更した。
- docstringを追加した。
- 本問は線形の二項間漸化式であるため、行列累乗を用いて`O(log n)`時間 で解くこともできる。
    - [行列累乗まとめ (競プロ)](https://zenn.dev/shibak3n/articles/f08a8ad67a7d14#fnref-89e9-2)
    - ただし、記事でも言及されているように、`O(log n)`という計算量解析には注意が必要。そのまま答えの値を計算するだけで考えると桁数が大きくなるため、足し算や掛け算が定数時間とみなせなくなる（大きい数ほど一度の計算に時間がかかる）可能性がある。ある数で割った余りを求めるなどの処理を行う場合は、`O(log n)`で計算できると考えられる。


## step3
```python
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return k
        previous_total_ways = k
        total_ways = k * k
        for _ in range(3, n + 1):
            total_ways, previous_total_ways = (k - 1) * (
                total_ways + previous_total_ways
            ), total_ways

        return total_ways
```
いつも1次元DPで、いくつかの変数を逐一、更新していく際には`tmp_foo`という一時変数を使って、元の値を保持しておくことが多かった。が、unpackして更新したほうが、コードが短くなり、可読性も上がるので、今後はできるだけこの書き方を使うことにしたい。ただし、上の例のように少し処理が複雑になると、可読性が下がるので難しいところもある。

## step4 (FB)

# 別解・模範解答
## メモ化再帰（hayashi-ayさんの解答）
- [276. Paint Fence by hayashi-ay · Pull Request #17 · hayashi-ay/leetcode · GitHub](https://github.com/hayashi-ay/leetcode/pull/17/files?short_path=50f7b63#diff-50f7b6331a7f8355594f718601d9bd00080e614a343f52dd67abdc08da922eba)
- メモ化再帰を用いて解く方法。
    - `@cache`デコレータを用いて、計算済みの値をキャッシュすることで、再帰的な計算を効率化している。

- 時間計算量：`O(n)`
- 空間計算量：`O(n)`（スタックの深さが最大`n`になるため）

```python

def cache(function):
    """
    my implementation of functools.cache
    """
    results_cache = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs)))
        if key in results_cache:
            return results_cache[key]
        result = function(*args, **kwargs)
        results_cache[key] = result
        return result

    return wrapper


class Solution:
    @cache
    def numWays(self, n: int, k: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return k
        if n == 2:
            return k * k

        return (k - 1) * (self.numWays(n - 1, k) + self.numWays(n - 2, k))
```

### cacheについて
- `@cache`デコレータも自作してみて、自分なりに調べた内容をまとめて技術記事にした。[Python functools.cacheを自作してみた。キーワード引数のキャッシュの仕様には注意 - Qiita](https://qiita.com/garudakai/items/ca35a0c9b399d875f491)
- LRUキャッシュも実装してみたい
    - [LRU Cache - LeetCode](https://leetcode.com/problems/lru-cache/description/)
    - [\[競プロ\]\[Python\] LRUキャッシュを実装する \| DevelopersIO](https://dev.classmethod.jp/articles/lru-cache-leetcode/)
    - [LRUキャッシュとLFUキャッシュをけっこう丁寧に実装します(Python) - Qiita](https://qiita.com/grouse324/items/8c7c48b17c4fbf246f44)


## 組み合わせの数を分けて数えて、最後に足す方法
つぎの2つのケースに分けて考える。
1. 末尾の二つのフェンスが同じ色の場合
2. 末尾の二つのフェンスが異なる色の場合

それぞれを別に計算して、最後に足す。

```python
class Solution:
    def numWays(self, n: int, k: int) -> int:
        one_consecutive = k
        two_consecutive = 0

        for _ in range(n - 1):
            new_one_consecutive = (k - 1) * (one_consecutive + two_consecutive)
            two_consecutive = one_consecutive
            one_consecutive = new_one_consecutive
            print(f"{one_consecutive=}, {two_consecutive=}")
        return one_consecutive + two_consecutive
```

# 次に解く問題の予告
- [LRU Cache - LeetCode](https://leetcode.com/problems/lru-cache/description/)
