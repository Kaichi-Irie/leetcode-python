#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#


# @lc code=start
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        all_permutations: list[list[int]] = []
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        head, tail = nums[0], nums[1:]
        # divide nums into two parts; head and tail.
        # find all the permutations of tail
        # and create an array by inserting head into each sub_permutation
        sub_permutations: list[list[int]] = self.permute(tail)
        for sub_permutation in sub_permutations:
            all_insertions: list[list[int]] = self.all_insertions(sub_permutation, head)
            all_permutations.extend(all_insertions)
        return all_permutations

    def all_insertions(self, nums: list[int], elem: int) -> list[list[int]]:
        """
        all_insertions returns all combinations of arrays obtained by inserting elem into nums.
        """
        if not nums:
            return [[elem]]
        all_insertions = []
        for i in range(len(nums) + 1):
            insertion = nums[:i] + [elem] + nums[i:]
            all_insertions.append(insertion)
        return all_insertions


# @lc code=end

# %%


# %%
