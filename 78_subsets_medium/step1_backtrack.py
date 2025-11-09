#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#


# @lc code=start
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        all_subsets = []
        self.backtrack(nums, nums, [], all_subsets)
        return all_subsets

    def backtrack(
        self,
        nums: list[int],
        remaining: list[int],
        chosen: list[int],
        all_subsets: list[list[int]],
    ) -> None:
        """
        the function backtrack count subset and add found subset to all_subsets. To count subset, backtrack choose an element num from remaining list for each step, and consider two patterns:
        1. the subset containing num
        2. the subset not containing num

        backtrack([1,2,3], [1,2,3], [], all)
        -> backtrack([1,2,3], [2,3], [1], all), backtrack([1,2,3], [2,3], [], all)

        backtrack([1,2,3], [2,3], [1], all)
        -> backtrack([1,2,3], [3], [2, 1], all), backtrack([1,2,3], [3], [1], all), ...etc
        """

        if not remaining:
            all_subsets.append(chosen)
            return
        num = remaining[0]

        self.backtrack(nums, remaining[1:], chosen.copy(), all_subsets)
        chosen.append(num)
        self.backtrack(nums, remaining[1:], chosen.copy(), all_subsets)


# @lc code=end
