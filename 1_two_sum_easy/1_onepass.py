#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,num in enumerate(nums):
            complement = target-num
            if complement in hashmap:
                return [i,hashmap[complement]]
            hashmap[num] = i
        return []
# @lc code=end
