#
# @lc app=leetcode id=276 lang=python3
#
# [276] Paint Fence
#


# @lc code=start
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


# @lc code=end
