#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greater_elements = []
        for num1 in nums1:
            next_greater_element = -1
            num1_found = False
            for num2 in nums2:
                if num2 == num1:
                    num1_found = True
                    continue
                elif not num1_found:
                    continue
                if num2 > num1:
                    next_greater_element = num2
                    break
            next_greater_elements.append(next_greater_element)

        return next_greater_elements
# @lc code=end
