#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start
from collections import defaultdict


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        sorted_nums = []
        int_min = -5*10**4
        int_max = 5*10**4
        for num in range(int_min, int_max+1):
            for _ in range(counts[num]):
                sorted_nums.append(num)

        return sorted_nums
# @lc code=end
