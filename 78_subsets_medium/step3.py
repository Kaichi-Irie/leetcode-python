#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#


# @lc code=start
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        all_subsets = []

        subset = []

        # insert every possible subset to all_subsets
        def backtrack(i: int) -> None:
            if i == len(nums):
                all_subsets.append(subset.copy())
                return
            # case 1. nums[i] is selected
            subset.append(nums[i])
            backtrack(i + 1)
            # case 2. nums[i] is not selected
            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return all_subsets


# @lc code=end
