#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#


# @lc code=start
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        all_permutations = []
        self.backtrack(nums, [], all_permutations)
        return all_permutations

    def backtrack(self, remaining, current, all_permutations) -> None:
        if not remaining:
            all_permutations.append(current)

        for i in range(len(remaining)):
            num = remaining[i]
            new_remaining = remaining[:i] + remaining[i + 1 :]
            self.backtrack(new_remaining, current + [num], all_permutations)


# @lc code=end
