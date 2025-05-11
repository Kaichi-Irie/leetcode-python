

from typing import List

#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,num1 in enumerate(nums):
            for j,num2 in enumerate(nums):
                if i==j:continue
                if num1+num2==target:
                    return [i,j]
        return []


# @lc code=end
