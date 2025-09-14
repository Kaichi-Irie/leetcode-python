# 問題へのリンク


# 言語
Python

# 問題の概要


# 自分の解法

## step1

```python
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0

        max_lengths_so_far = [1] * len(nums)

        for i in range(1, len(nums)):
            length = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    length = max(length, max_lengths_so_far[j])
            max_lengths_so_far[i] = length + 1
        return max(max_lengths_so_far)
```

- 変数名がうまくつけられなかった
- 時間計算量も最適でない

`nums`の要素数を`n`とすると、
- 時間計算量：`O(n^2)`
- 空間計算量：`O(n)`

## step2

```python
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0

        # max_length[i] is the maximum length of increasing subsequences that ends at nums[i]
        max_lengths = [1] * len(nums)
        for i in range(len(nums)):
            max_previous_length = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    max_previous_length = max(max_previous_length, max_lengths[j])
            max_lengths[i] = max_previous_length + 1
        return max(max_lengths)
```

## step3

## step4 (FB)



# 別解・模範解答

`min_tails_linear.py`

```python
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        # min_tails[i] is the minimum number of the tails of increasing subsequences with length (i+1)
        if not nums:
            return 0
        min_tails = [nums[0]]
        for num in nums[1:]:
            if min_tails[-1] < num:
                min_tails.append(num)
                continue
            for i, tail in enumerate(min_tails):
                if num <= tail:
                    min_tails[i] = num
                    break
        return len(min_tails)
```

- `min_tails[i]`は長さ`i + 1`の増加部分列の最小の末尾要素を表す
- 非常にエレガントだが、なぜこれで正しいのか直感的に理解するのは難しい
- 時間計算量：`O(n^2)`
- 空間計算量：`O(n)`
    - 最悪、`nums`が昇順にソートされている場合、`tails`の長さは`n`になる


`mins_tails`は常に昇順にソートされているので、`num`が`min_tails`のどこに入るかを二分探索で探せる時間計算量は`O(log n)`になる



`min_tails_binary_search_bisect.py`
```python
import bisect


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        min_tails = [nums[0]]
        for num in nums[1:]:
            j = bisect.bisect_left(min_tails, num)
            if j == len(min_tails):
                min_tails.append(num)
            else:
                min_tails[j] = num
        return len(min_tails)
```


- 時間計算量：`O(log n)`
- 空間計算量：`O(n)`

# 想定されるフォローアップ質問

## CS 基礎

## システム設計

## その他

# 次に解く問題の予告
- Permutations
