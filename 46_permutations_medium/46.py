#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#


# @lc code=start
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        all_permutations = []
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            print([nums])
            return [nums]
        last_elem: int = nums[-1]
        sub_permutations: list[list[int]] = self.permute(nums[: len(nums) - 1])

        for perm in sub_permutations:
            for j in range(len(perm) + 1):
                new_perm: list = perm[:j] + [last_elem] + perm[j:]

                all_permutations.append(new_perm)

        return all_permutations


# @lc code=end

# %%


# %%
