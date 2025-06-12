#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#


# @lc code=start
from functools import cache


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        all_permutations = []
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        num0 = nums[0]
        # think of a subarray that num is removed.
        # all the permutations of this subarray is
        sub_permutations = self.permute([num for num in nums if num != num0])
        for sub_permutation in sub_permutations:
            all_insertions = self.all_insertions(sub_permutation, num0)
            for insertion in all_insertions:
                all_permutations.append(insertion)
        return all_permutations

    def all_insertions(self, nums: list[int], elem: int) -> list[list[int]]:
        insertions = []
        if not nums:
            insertions = [[elem]]
            # print(f"{nums=}, {elem=}, {insertions=}")
            return insertions

        for i in range(len(nums) + 1):
            insertion = nums[:i] + [elem] + nums[i:]
            insertions.append(insertion)
        # print(f"{nums=}, {elem=}, {insertions=}")

        return insertions


# @lc code=end

# %%


# %%
