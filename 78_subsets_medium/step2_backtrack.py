#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#


# @lc code=start
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        all_subsets: list[list[int]] = []
        subset = []

        def create_subset(i: int) -> None:
            if i == len(nums):
                all_subsets.append(subset[:])
                return
            subset.append(nums[i])
            create_subset(i + 1)
            subset.pop()
            create_subset(i + 1)

        create_subset(0)
        return all_subsets


# @lc code=end
