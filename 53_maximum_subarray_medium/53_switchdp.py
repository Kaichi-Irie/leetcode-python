#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
from typing import List


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        INF = pow(10, 4) + 9
        # DPによる解法の説明：
        # 問題：連続する部分配列のうち、最大の和を持つものを見つける

        # DP定義：
        # dp[i][*] では，インデックスiまでの部分配列に対する最大部分和を考える
        # dp[i][1]: 右端の要素nums[i]を「必ず含む」部分配列の最大和
        # dp[i][0]: 右端の要素nums[i]を「含まない」部分配列の最大和

        # DP漸化式：
        # 1. dp[i][1]（nums[i]を含む場合）：
        #    - dp[i-1][1] + nums[i]：前の要素までの最大部分和にnums[i]を追加
        #    - nums[i]：新しく部分配列を開始（前の部分和が負の場合に有効）
        #    上記2つの大きい方を選択

        # 2. dp[i][0]（nums[i]を含まない場合）：
        #    - dp[i-1][1]：i-1番目までの要素で、最後の要素を含む最大部分和
        #    - dp[i-1][0]：i-1番目までの要素で、最後の要素を含まない最大部分和
        #    上記2つの大きい方を選択

        # 初期条件：
        # dp[0][1] = nums[0]：最初の要素のみを含む場合
        # dp[0][0] = -INF：最初の要素を含まない場合（存在しないので非常に小さい値）

        # dp = [[-INF, -INF] for _ in range(N)]
        # dp[0][1] = nums[0]
        # for i in range(1, N):
        #     dp[i][1] = max(dp[i - 1][1] + nums[i], nums[i])
        #     dp[i][0] = max(dp[i - 1][1], dp[i - 1][0])

        # 省メモリver.
        dp_0 = -INF
        dp_1 = nums[0]
        for i in range(1, N):
            dp_0 = max(dp_0, dp_1)
            dp_1 = max(dp_1 + nums[i], nums[i])
        ans = max(dp_0, dp_1)
        return ans


# @lc code=end
