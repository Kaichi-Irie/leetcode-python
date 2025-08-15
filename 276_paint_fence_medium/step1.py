#
# @lc app=leetcode id=276 lang=python3
#
# [276] Paint Fence
#


# @lc code=start
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


# @lc code=end
