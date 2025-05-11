#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#
from typing import List

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        S1=set(nums1)
        S2=set(nums2)
        ans_list = []
        for n in S1:
            if n in S2:
                ans_list.append(n)
        return ans_list
# @lc code=end
