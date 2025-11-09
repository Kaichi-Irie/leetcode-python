#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#


# @lc code=start
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        num_all_subsets = pow(2, len(nums))
        all_subsets: list[list[int]] = []

        for subset_binary_expression in range(num_all_subsets):
            subset: list[int] = []
            for i, num in enumerate(nums):
                is_num_selected = self._digit_i(subset_binary_expression, i)
                if is_num_selected:
                    subset.append(num)
            all_subsets.append(subset)

        return all_subsets

    def _digit_i(self, num: int, i: int) -> int:
        """
        _digit_i returns i th binary digit value of num.
        e.g. _digit_i(4,0) = _digit_i(4,1)  = 0, _digit_i(4,2) = 1
        """

        return (num >> i) & 1


# @lc code=end
