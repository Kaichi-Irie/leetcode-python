#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def find_min_index() -> int:
            left = 0
            right = len(nums) - 1

            while left < right:
                mid = (right + left) // 2
                if nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
            return left

        def binary_search(left_bound, right_bound, target) -> int:
            left = left_bound
            right = right_bound

            while left <= right:
                mid = (right + left) // 2
                if nums[mid] == target:
                    return mid
                if target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            return NOT_FOUND

        NOT_FOUND = -1
        min_idx = find_min_index()

        if nums[min_idx] <= target <= nums[-1]:
            return binary_search(min_idx, len(nums) - 1, target)
        else:
            return binary_search(0, min_idx - 1, target)


# @lc code=end
