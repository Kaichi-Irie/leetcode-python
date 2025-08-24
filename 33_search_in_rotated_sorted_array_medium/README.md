# 問題へのリンク
[Search in Rotated Sorted Array - LeetCode](https://leetcode.com/problems/search-in-rotated-sorted-array/)

# 言語
Python

# 問題の概要
rotateされたソート済み配列から特定の値`target`を検索する問題です。配列は回転されているため、通常の二分探索ではなく、回転された状態を考慮した二分探索を行う必要があります。


# 自分の解法

## step1

2回二分探索を用いて、回転されたソート済み配列から特定の値を検索する解法。1回目の二分探索で、配列の最小値を見つけ、`shift`（どのくらい配列がrotateされたか） の値を求める。2回目の二分探索で、`shift`を考慮して元の配列のインデックスを計算し、通常の二分探索で`target`を検索する。インデックスの計算が毎回必要になるため、少し複雑な実装になる。
- 時間計算量：`O(logn)`
- 空間計算量：`O(1)`

```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def find_rotated_shift() -> int:
            left = 0
            right = len(nums) - 1
            if nums[left] <= nums[right]:
                return 0
            while (right - left) > 1:
                mid = (right + left) // 2
                if nums[mid] <= nums[right]:
                    right = mid
                else:
                    left = mid
            return right

        def shifted_index(index: int, shift: int) -> int:
            return (index + shift) % len(nums)

        NOT_FOUND = -1

        shift = find_rotated_shift()
        left = 0
        right = len(nums) - 1
        if target < nums[shifted_index(left, shift)]:
            return NOT_FOUND
        elif target > nums[shifted_index(right, shift)]:
            return NOT_FOUND
        elif nums[shifted_index(right, shift)] == target:
            return shifted_index(right, shift)

        mid = 0
        while (right - left) > 1:
            mid = (right + left) // 2
            if target < nums[shifted_index(mid, shift)]:
                right = mid
            else:
                left = mid
        if nums[shifted_index(left, shift)] == target:
            return shifted_index(left, shift)
        else:
            return NOT_FOUND
```


## step2

```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            # midが左側の領域にいる
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # midが右側の領域にいる
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        NOT_FOUND = -1
        return NOT_FOUND
```

- 模範解答を見て二分探索を1回だけ用いる解法（ワンパス二分探索）に変更した。条件分岐が複雑で、二回に分けて考える解法の方がわかりやすいのでは？とも考えたが、次のように考えるとこの場合分けが漏れのないものだと自信を持てるようになった。
- 原則：「回転した配列を真ん中（`mid`）で分割すると、`[left,mid]`もしくは`[mid,right]`のいずれか一方はソートされた配列になっている。」
- 場合1：`nums[left] <= nums[mid]` の場合、左側の部分配列はソートされている。
    - この場合、`target`が左側にあるかどうかを確認し、そうであれば左側を探索する。もしそうでなければ左側はもう探索する必要がないので、この範囲を捨て、右側を探索するようにする。
- 場合2：`nums[left] > nums[mid]` の場合、逆に`nums[mid]<=nums[right]`が成り立ち、右側の部分配列はソートされている。
    - この場合、`target`が右側にあるかどうかを確認し、もしそうであれば右側を探索する。そうでなければ右側はもう探索する必要がないので、この範囲を捨て、左側を探索するようにする。
- 本問では`target`に一致するindexを探すので、添え字の区間を`[left,mid)`,`[mid,mid]`,`(mid,right]`の３つに分けて考えるとわかりやすい。
- 基本的には閉区間でインデックスを指す二分探索がわかりやすいと感じている。
- `while left <= right`を使った二分探索は初めて。
    - `while left <= right`: **特定の値を「見つける」** ための探索。ループの **中で** 答えが見つかる。答えが見つかり次第、値を返すので、ループを走査し終えたときは答えが見つからなかったことを意味する。
    - `while left < right`: **条件を満たす「境界」**（例: 挿入位置、最初のtrueなど）を探すための探索。ループが **終わった後** に答えが確定する。
    - これまでは境界を求めるために `while (right-left)>1` という条件で探索を行っていたが、これでは前処理が少し複雑になる。`while left < right` に変更することで、よりシンプルに実装できるようになるが、`left` と `right`の更新が`mid`, `mid+1`, `mid-1`のいずれかになることに気をつける必要がある。（`while (right-left)>1`の場合は、`mid`だけで更新できる）→めぐる式を採用すれば解決しそうだが、今度は読み手に伝わるかどうかが問題となる。


## step3

```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid

            # [left, mid]がソート済み配列の場合
            if nums[left] <= nums[mid]:
                # target が [left, mid]の範囲内にある場合
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # それ以外（[left, mid]の範囲を捨てる）
                else:
                    left = mid + 1
            # [mid, right]がソート済み配列の場合
            else:
                # target が [mid,right]の範囲内にある場合
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # それ以外（[mid,right]の範囲を捨てる）
                else:
                    right = mid - 1
        NOT_FOUND = -1
        return NOT_FOUND
```

- 時間計算量：`O(logn)`
- 空間計算量：`O(1)`

# 別解 区間を分ける
```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # 最小値のインデックスを求める
        def find_min_index(nums):
            left = 0
            right = len(nums) - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
            return left

        min_index = find_min_index(nums)

        # min_indexを基準に2つの区間に分けて探索
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # 左側の区間を探索
            if mid < min_index:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # 右側の区間を探索
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        NOT_FOUND = -1
        return NOT_FOUND
```

- こちらも二分探索を2回用いる解法である。最初に最小値のインデックス`min_index`を求めた後、`min_index`を基準にして2つの区間に分けて探索を行う。
- 具体的には、`nums[:min_index]`と`nums[min_index:]`の2つの部分配列に分けて、それぞれに対して通常の二分探索を行う。
    - スライスを作るとメモリを消費するので、インデックスで計算を進める。

- 時間計算量：`O(logn)`
- 空間計算量：`O(1)`

# 次に解く問題の予告
- [Coin Change - LeetCode](https://leetcode.com/problems/coin-change/)
