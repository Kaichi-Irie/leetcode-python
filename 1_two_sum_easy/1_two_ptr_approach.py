#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        i = 0
        j = len(sorted_nums) - 1
        while sorted_nums[i] + sorted_nums[j] < target:
            i += 1

        while i < j:
            n_i, n_j = sorted_nums[i], sorted_nums[j]
            if n_i + n_j == target:
                i0 = j0 = -1
                for idx, num in enumerate(nums):
                    if num == n_i and i0 == -1:
                        i0 = idx
                    elif num == n_j and j0 == -1:
                        j0 = idx
                return [i0, j0]
            elif n_i + n_j > target:
                j -= 1
            else:
                i += 1
                j += 1
        return []


# @lc code=end
