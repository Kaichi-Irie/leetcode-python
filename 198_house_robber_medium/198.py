#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
from typing import List


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 1:
            return nums[0]

        # dp[i]: 1,...,i番目までの家を対象にしたときの，盗める金額の最大値．
        # NでなくN+1まで用意して1-indexedにしているのはmax()を活用することで初期化を書かないようにするため．でもサボらず初期化を書いた方がコードはわかりやすい
        # dp = [0] * (N + 1)
        # for i in range(1, N + 1):
        #     dp[i] = max(dp[max(i - 1, 0)], dp[max(i - 2, 0)] + nums[i - 1])
        # return dp[N]
        # 初期化のコードを書いたver.
        dp = [0] * N
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])
        for i in range(2, N):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[N - 1]


# @lc code=end
