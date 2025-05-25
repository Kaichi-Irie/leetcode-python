#
# @lc app=leetcode id=2178 lang=python3
#
# [2178] Maximum Split of Positive Even Integers
#


# @lc code=start
class Solution:
    def maximumEvenSplit(self, finalsum: int) -> list[int]:
        # if the finalsum is odd, then return empty list
        if finalsum % 2 == 1:
            return []

        # for k = 2, 4, ..., insert k into max_split if possible.
        # at last, adjust last element to make the sum of max_split equal to finalsum
        max_split = []
        current_sum = 0
        k = 2
        while current_sum + k <= finalsum:
            # insert k
            max_split.append(k)
            current_sum += k
            k += 2

        # adjust last element value to make the sum of max_split equal to finalsum
        remaining = finalsum - current_sum
        max_split[-1] += remaining
        return max_split


# @lc code=end

# %%
