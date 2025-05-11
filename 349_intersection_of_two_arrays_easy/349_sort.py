#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#
from typing import List


# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        length1 = len(nums1)
        length2 = len(nums2)

        MAX = 10000
        nums1.append(MAX)
        nums2.append(MAX)
        ans_list = []
        ptr1 = 0
        ptr2 = 0
        previously_added = -1
        while True:
            if ptr1 == length1 and ptr2 == length2:
                return ans_list
            n1 = nums1[ptr1]
            n2 = nums2[ptr2]
            if n1 == n2:
                ptr1 += 1
                ptr2 += 1
                if n1 != previously_added:
                    ans_list.append(n1)
                    previously_added = n1
            elif n1 < n2:
                ptr1 += 1
            else:
                ptr2 += 1


# @lc code=end
