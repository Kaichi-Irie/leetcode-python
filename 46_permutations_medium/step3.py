#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
import itertools


# @lc code=start
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if not nums:
            return []
        if len(nums) == 1:
            return [nums]
        all_permutations = []
        head, tail = nums[0], nums[1:]
        # all the permutations of tail
        sub_permutations = self.permute(tail)
        # insert head into each sub_permutation
        for sub_permutation in sub_permutations:
            all_inserted_arrays = self.generate_all_inserted_arrays(
                sub_permutation, head
            )
            all_permutations.extend(all_inserted_arrays)
        return all_permutations

    def generate_all_inserted_arrays(
        self, nums: list[int], elem: int
    ) -> list[list[int]]:
        if not nums:
            return [elem]
        all_inserted_arrays: list[list[int]] = []
        for i in range(len(nums) + 1):
            inserted_array: list = nums[:i] + [elem] + nums[i:]
            all_inserted_arrays.append(inserted_array)
        return all_inserted_arrays


# @lc code=end
