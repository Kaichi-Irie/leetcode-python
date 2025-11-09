# 問題へのリンク
[300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)

# 言語
Python

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

`step3_bruteforce.py`
```python
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        left_max_lengths = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    left_max_lengths[i] = max(
                        left_max_lengths[i], left_max_lengths[j] + 1
                    )

        return max(left_max_lengths)
```
- こっちはすらすら書ける


`step3_binary_search.py`
```python
class Solution:
    def bisect_left(self, nums: list[int], target: int) -> int:
        if not nums:
            return 0
        left = -1
        right = len(nums)
        while right - left > 1:
            mid = (right + left) // 2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid
        return right

    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        tails = []
        for num in nums:
            index = self.bisect_left(tails, num)
            if index == len(tails):
                tails.append(num)
                continue
            tails[index] = num
        return len(tails)
```

- `tails`は常に昇順にソートされているので、`num`が`tails`のどこに入るかを二分探索。これは覚えていないと書けない
- `left=-1`, `right=len(nums)`から始めると、`mid=-1`や`mid=len(nums)`になるのではないかと不安に思っていたが、`while right - left > 1`の条件でループするので、ループの中では`right - left`は常に2以上になるので、`left < mid < right`が保証される。返り値は`right`なので、`len(nums)`が返ることはある。
- ちなみに`bisect_right`の実装は

```python
def bisect_right(nums: list[int], target: int) -> int:
    left = -1
    right = len(nums)
    while right - left > 1:
        mid = (right + left) // 2
        if target < nums[mid]:
            right = mid
        else:
            left = mid
    return right
```

## step4 (FB)

- `max_lengths_so_far`は`index_to_max_length`や`max_length_by_index`、`max_length_ending_at_index`などの方が良い


```python
for i in range(len(nums)):
    for j in range(i):
        if nums[j] < nums[i]:
            left_max_lengths[i] = max(
                left_max_lengths[i], left_max_lengths[j] + 1
            )
```
は

```python
for i in range(len(nums)):
    left_max_length[i] = max(
        [left_max_length[j] + 1 for j in range(i) if nums[j] < nums[i]],
        default = 1
        )
```
とも書ける。余分にメモリは確保してしまうが、オーダーには影響しない程度。むしろ、二重ループに強弱が出てわかりやすいと感じた。つまり、内部の`j`のループは`i`のためにmaxを取るために回しているもので従属的である、と伝わりやすいと感じた。逆に多重ループが完全に独立している（直積である）ときには、`itertools.product`を使えば良い。
- `max`の`default`引数は空のイテレータを渡した時の返り値を設定できる。`max([])`をそのまま実行すると、`ValueError: max() iterable argument is empty`が出る。

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
- もし `bisect_left` ではなく `bisect_right` を使った場合、結果は変わりますか？変わる場合、どのような入力で変わりますか？変わらない場合、その理由は何ですか？
    - 本問では、`bisect_left` と `bisect_right` のどちらを使用しても結果は変わらない。なぜなら、求めるLISは"strictly increasing"であり、`tails`配列に同じ値が存在することはないからである。しかし、もし問題が"non-decreasing"なLISを求めるものであれば、`bisect_right`を使用することで、同じ値を持つ要素が`tails`に追加される可能性があり、結果が変わることになる。その場合は`bisect_right`を使用することで、同じ値を持つ要素がLISに含まれることを許容することになる。
- このアルゴリズムではLISの『長さ』しか分かりませんが、実際の部分列そのものを復元するには、どのような変更が必要になりますか？
    - このアルゴリズムでは、実際にはLISの「長さ」に加えて「末尾の要素」もわかる。そのため、末尾から



# 次に解く問題の予告
- [Subarray Sum Equals K - LeetCode](https://leetcode.com/problems/subarray-sum-equals-k/description/)
- [String to Integer (atoi) - LeetCode](https://leetcode.com/problems/string-to-integer-atoi/description/)
- [Number of Islands - LeetCode](https://leetcode.com/problems/number-of-islands/description/)
