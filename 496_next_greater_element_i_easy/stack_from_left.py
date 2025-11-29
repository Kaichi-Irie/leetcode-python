#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        next_greater_elements = {}
        for num in nums2:
            while stack:
                num_left = stack.pop()
                if num <= num_left:
                    stack.append(num_left)
                    break
                next_greater_elements[num_left] = num
            stack.append(num)

        while stack:
            num = stack.pop()
            next_greater_elements[num] = -1

        results = []
        for num in nums1:
            results.append(next_greater_elements[num])
        return results
# @lc code=end
