# 問題へのリンク
[560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

# 言語
Python


# 自分の解法
- `nums`に負の数が含まれなければ、two pointersでTC: `O(n)`/ SC: `O(1)`で解けるが、負の数が含まれるので、two pointersは使えない。
    - 累積和に対して二分探索をして`O(n log n)`という解法もある。
- すべての数に一律に大きな値（`-min(nums)`など）を足して累積和を非負にする方法も考えたが、それでは累積和が「要素数×ずらした値」の分だけずれるので、うまくいかない。

## step1
二重ループを回す方法
```python
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        num_subarrays = 0
        # cumsums[i] = sum(nums[:i])
        # sum(nums[i:j]) = cumsums[i] - cumsums[j]
        cumsums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            cumsums[i + 1] = cumsums[i] + nums[i]

        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                sum_from_i_to_j = cumsums[j] - cumsums[i]
                if sum_from_i_to_j == k:
                    num_subarrays += 1

        return num_subarrays
```

`n`を`nums`の長さとすると、
- 時間計算量：`O(n^2)`
- 空間計算量：`O(n)`

- この空間計算量は`O(1)`にできる





- `cumsum`の求め方は以下のような方法もある。
```python
cumsums = [0]
for num in nums:
    cumsums.append(cumsums[-1] + num)
```
(ref: https://github.com/tokuhirat/LeetCode/pull/16/files?short_path=d4900f9#diff-d4900f989c6f9680b8e8144658ef8f10d6025523b2c0c63bed653dcdcc4fc290)

## step2
空間計算量を`O(1)`にする方法
```python
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        num_subarrays = 0
        for i in range(len(nums)):
            subarray_sum = 0  # sum(nums[i:j+1])
            for j in range(i, len(nums)):
                subarray_sum += nums[j]
                if subarray_sum == k:
                    num_subarrays += 1
        return num_subarrays
```

- `cumsum`は`cumsums[i] = sum(nums[:i])`と定義すると、元の配列より1だけ長くなるので、添え字の管理が面倒になる点に注意する。特に、本解法のようにforループを1度だけ回す場合、`range`の範囲をどうするかがポイントになる＆バグを生みやすい。
    - `cumsums[i] = sum(nums[:i+1])`と定義すると、`cumsums`の長さは`len(nums)`と同じになるが、`cumsums[i] - cumsums[i-1] = nums[i]`が`i=0`のときに成り立たないので、条件分岐が余分に必要になる。
- cumulative sum はprefix sumとも呼ばれる。
    - cf. https://en.wikipedia.org/wiki/Prefix_sum



## step3

`step3_1.py` (20 min)
```python
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        """
        Find the number of pairs (i,j) such that sum(nums[i:j]) == k (0<=i<j<=n).
        This can be found as below:
        for each j = 1, ..., len(nums), find the number of i (0<=i<j) that satisifes nums[:j] -k == nums[:i].
        Note that nums[:0] is defined as 0.
        """
        num_subarrays = 0
        # sum(nums[:i]) -> count
        subarray_sum_count: dict[int, int] = defaultdict(int)
        sum_to_j = 0
        # Add sum(nums[:0]) = 0
        subarray_sum_count[0] = 1
        for j in range(1, len(nums) + 1):
            sum_to_j += nums[j - 1]  # sum(nums[:j])
            count = subarray_sum_count[sum_to_j - k]
            num_subarrays += count
            subarray_sum_count[sum_to_j] += 1
        return num_subarrays
```
- `sum_to_j`は`prefix_sum`の方が適切かも
- `subarray_sum_count` も `prefix_sum_count` の方が適切かも

テストケース
<!-- subarraySum([1], 1) == 1
subarraySum([1], 0) == 0
subarraySum([1, 1, 1], 3) == 1
subarraySum([1, 1, 1], 2) == 2
subarraySum([1, -1, 1, -1], 0) == 4 -->

- 単一要素:`nums=[1]`, `k=1` -> `1`、`nums=[1]`, `k=0` -> `0`
- 同じ要素が複数ある: `nums=[1, 1, 1]`, `k=3` -> `1`、`nums=[1, 1, 1]`, `k=2` -> `2`
- 標準的なケース: `nums=[1, 2, 3, -3, 3]`, `k=3` -> `4`
- k=0: `nums=[1, -1, 1, -1]`, `k=0` -> `4`
- 0を多く含む: `nums=[0, 1, 0]`, `k=1` -> `4`
    - 足し算では、0が（単位元なので）特殊なケースになることが多い
    - 掛け算では、1
- kが負: `nums=[-1, -1, -1]`, `k=-2` -> `2`
- 空配列: `nums=[]`, `k=0` -> `0`、`nums=[]`, `k=1` -> `0`

## step4 (FB)



# 別解・模範解答
## ハッシュマップを使う方法
時間計算量を`O(n)`にできる。
```python
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # k = nums[i:j] = cumsums[j] - cumsums[i]
        # if cumsums[j]-k in cumsum_hashmap for j in i+1, ..., then OK
        num_subarrays = 0
        # cumsums[i] = sum(nums[:i])
        cumsums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            cumsums[i + 1] = cumsums[i] + nums[i]

        hashmap: dict[int, int] = defaultdict(int)
        for i in range(len(nums) + 1):
            num_subarrays += hashmap[cumsums[i] - k]
            hashmap[cumsums[i]] += 1
        return num_subarrays
```

- Subarray自体は必要なくて、その数だけが必要であることがミソ。数だけなら、ハッシュマップで管理すれば、`O(1)`でアクセスできる。
    - `cumsums`を使う解法ではSubarray自体が求まる
- ただし、`cumsums`の解法の空間計算量を`O(1)`にした解法とは時間計算量と空間計算量のトレードオフの関係にあるので、どちらが良いかは場合による。

- 時間計算量：`O(1)`
- 空間計算量：`O(n)`

## `nums`が正の数のみを含む場合（two pointers）
```python
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        """
        Find the subarraySum in O(n) when nums have positive elements.
        """
        if not nums:
            return 0
        num_subarrays = 0
        subarray_sum = 0
        left = 0
        for right in range(len(nums)):
            subarray_sum += nums[right]
            while left < right and subarray_sum > k:
                subarray_sum -= nums[left]
                left += 1

            if subarray_sum == k:
                num_subarrays += 1

        return num_subarrays
```
- ただし、`nums`に0が含まれる場合は、結構複雑になる


# 想定されるフォローアップ質問
- この実装の最悪空間使用量は？どうすれば実使用メモリを抑えられますか？
    - `defaultdict`の代わりに`dict.get`を使えば、メモリ使用量を抑えられる可能性がある。

# 次に解く問題の予告
- [String to Integer (atoi) - LeetCode](https://leetcode.com/problems/string-to-integer-atoi/description/)
- [Number of Islands - LeetCode](https://leetcode.com/problems/number-of-islands/description/)
