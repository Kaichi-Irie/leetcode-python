#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid

            # [left, mid]がソート済み配列の場合
            if nums[left] <= nums[mid]:
                # target が [left, mid]の範囲内にある場合
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # それ以外（[left, mid]の範囲を捨てる）
                else:
                    left = mid + 1
            # [mid, right]がソート済み配列の場合
            else:
                # target が [mid,right]の範囲内にある場合
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # それ以外（[mid,right]の範囲を捨てる）
                else:
                    right = mid - 1
        NOT_FOUND = -1
        return NOT_FOUND


# @lc code=end
