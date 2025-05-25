#
# @lc app=leetcode id=2178 lang=python3
#
# [2178] Maximum Split of Positive Even Integers
#

import math


# @lc code=start
class Solution:
    def maximumEvenSplit(self, finalsum: int) -> list[int]:
        # if finalsum is an odd number, then return empty list
        if finalsum % 2 == 1:
            return []
        # Solve the problem in a greedy way.
        # Let's define S_n := 2+4+...+2n =n(n+1), and
        # n := int(sqrt(finalsum)) (sqrt_of_finalsum)
        # S_(n-1) < finalsum <?> S_n < S_(n+1)

        # math.isqrt returns integer, which does not have any floating point errors.
        sqrt_of_finalsum = math.isqrt(finalsum)
        split = []
        for k in range(1, sqrt_of_finalsum):
            split.append(2 * k)

        # sum_sofar = S_(n-1) < finalsum
        sum_sofar = sum(split)
        # remaining = finalsum - S_(n-1)
        remaining = finalsum - sum_sofar

        # case1. finalsum = 2
        if len(split) == 0:
            split = [remaining]
            return split

        last_elem = split[-1]  # (= 2*(n-1))
        # case2. if last_elem < remaining, then split = [2,..., last_elem, remaining]
        if remaining > last_elem:
            split.append(remaining)
        # case3. if remaining <= last_elem, then split = [2,..., last_elem + remaining]
        else:
            split[-1] = last_elem + remaining
        return split


# @lc code=end

# %%
