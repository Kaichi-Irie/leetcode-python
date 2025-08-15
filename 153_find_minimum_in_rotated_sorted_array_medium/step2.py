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

        left = 0
        right = len(nums) - 1
        # Array is not rotated (Already sorted in ascending order)
        if nums[left] <= nums[right]:
            return nums[left]

        # nums[right] < nums[left] always holds during binary search
        while (right - left) > 1:
            mid = left + (right - left) // 2
            if nums[mid] <= nums[right]:
                right = mid
            # nums[left] <= nums[mid]
            else:
                left = mid

        # nums[left]: largest, and nums[right]: smallest
        return nums[right]


# @lc code=end
