#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#


# @lc code=start
class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        # case 1. already sorted
        if nums[left] <= nums[right]:
            return nums[left]

        # case 2. rotated
        # find min using binary search.  nums[left] > nums[right] always holds
        while right - left > 1:
            mid = left + (right - left) // 2
            if nums[left] < nums[mid]:
                left = mid
            else:
                right = mid

        return nums[right]


# @lc code=end
