#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: list[int]) -> int:
        def is_index_value_leq_to_last(index: int) -> bool:
            if index < 0 or len(nums) <= index:
                return False
            return nums[-1] >= nums[index]

        left = -1
        right = len(nums) - 1
        while (right - left) > 1:
            mid = (right + left) // 2
            if is_index_value_leq_to_last(mid):
                right = mid
            else:
                left = mid

        return nums[right]


# @lc code=end
