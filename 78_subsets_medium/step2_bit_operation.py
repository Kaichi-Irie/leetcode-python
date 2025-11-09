#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#


# @lc code=start
# TC: O(n*2^n)
# SC: O(n*2^n)
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        all_subsets: list[list[int]] = []
        num_subsets = pow(2, len(nums))
        for subset_expression in range(num_subsets):
            subset: list[int] = []
            for i, num in enumerate(nums):
                # i th digit of subset_expression represents if nums[i] is inclued in subset or not
                is_num_selected = self._ith_binary_digit(subset_expression, i)
                if is_num_selected:
                    subset.append(num)
            all_subsets.append(subset)
        return all_subsets

    def _ith_binary_digit(self, num: int, i: int) -> int:
        return (num >> i) & 1


# @lc code=end
