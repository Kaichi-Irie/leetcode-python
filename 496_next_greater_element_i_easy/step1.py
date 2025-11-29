#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greater_elements = {}
        stack = []
        for num in nums2[::-1]:
            next_greater_element = -1
            while stack:
                num_right = stack.pop()
                if num >= num_right:
                    continue
                next_greater_element = num_right
                stack.append(num_right)
                break
            next_greater_elements[num] = next_greater_element
            stack.append(num)

        results = []
        for num in nums1:
            results.append(next_greater_elements[num])
        return results

# @lc code=end
