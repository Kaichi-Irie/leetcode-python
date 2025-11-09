#
# @lc app=leetcode id=276 lang=python3
#
# [276] Paint Fence
#


# @lc code=start
class Solution:
    def numWays(self, n: int, k: int) -> int:
        """
        Find the number of ways using dynamic programming.
        total_ways[n]: number of possibilities using n posts with k different colorss (supporse that k is given).
        To compute total_ways[n], we can consider two exclusive cases:
        1. colors of fence `n` and `n-1` are different: (k-1) * total_ways[n-1]
        2. colors of fence `n` and `n-1` are same: (k-1) * total_ways[n-2]

        Then, following recursive holds for all n = 3, 4, ...;
        - total_ways[1] = k
        - total_ways[2] = k*k
        - total_ways[n] = (k-1) * total_ways[n-1] + (k-1) * total_ways[n-2]

        For better performance, we use update two variables, total_ways and preivious_total_ways, iteratively instead of allocating an array.
        """
        if n <= 0:
            return 0
        if n == 1:
            return k

        preivious_total_ways = k
        total_ways = k * k
        for _ in range(3, n + 1):
            new_total_ways = (k - 1) * (total_ways + preivious_total_ways)
            total_ways, preivious_total_ways = new_total_ways, total_ways
        return total_ways


# @lc code=end
