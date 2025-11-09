#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#


# @lc code=start
class Solution:
    def findMin(self, nums: list[int]) -> int:
        if not nums:
            raise ValueError("nums must have at least one element.")
        elif len(nums) <= 2:
            return min(nums)

        L = 0
        R = len(nums) - 1
        # no rotation
        if nums[L] <= nums[R]:
            return nums[L]

        # nums[R] < nums[L] always holds
        while (R - L) > 1:
            mid = (R + L) // 2
            if nums[mid] < nums[R]:
                R = mid
            #  nums[L] < nums[mid]:
            else:
                L = mid

        # R-L = 1, nums[L]: largest, and nums[R]: smallest
        return nums[R]


# @lc code=end
