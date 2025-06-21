#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#


# @lc code=start
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def generate_subsets_before_index(index: int) -> list[list[int]]:
            """
            generate_subsets_before_index(index) generates subsets of list nums[:index]
            """
            if index == 0:
                return []
            if index == 1:
                return [[], [nums[0]]]
            elif index > len(nums):
                index = len(nums)

            all_subsets: list[list[int]] = []
            # sub_subsets is a list of all subsets of nums[0:index-1]
            sub_subsets: list[list[int]] = generate_subsets_before_index(index - 1)
            last_num = nums[index - 1]

            for subset in sub_subsets:
                all_subsets.append(subset.copy())
                subset.append(last_num)
                all_subsets.append(subset.copy())

            return all_subsets

        return generate_subsets_before_index(len(nums))


# @lc code=end
