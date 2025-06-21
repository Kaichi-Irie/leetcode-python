#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#


# @lc code=start
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        all_subsets: list[list[int]] = []
        num_subsets = pow(2, len(nums))
        for subset_expression in range(num_subsets):
            subset: list[int] = []
            for i, num in enumerate(nums):
                # i th digit of subset_expression represents if nums[i] is inclued in subset or not
                include_i = (subset_expression >> i) & 1
                if include_i:
                    subset.append(num)
            all_subsets.append(subset)
        return all_subsets
    

# @lc code=end
