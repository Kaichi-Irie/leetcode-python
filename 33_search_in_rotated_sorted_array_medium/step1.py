#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def find_rotated_shift() -> int:
            left = 0
            right = len(nums) - 1
            if nums[left] <= nums[right]:
                return 0
            while (right - left) > 1:
                mid = (right + left) // 2
                if nums[mid] <= nums[right]:
                    right = mid
                else:
                    left = mid
            return right

        def shifted_index(index: int, shift: int) -> int:
            return (index + shift) % len(nums)

        NOT_FOUND = -1

        shift = find_rotated_shift()
        left = 0
        right = len(nums) - 1
        if target < nums[shifted_index(left, shift)]:
            return NOT_FOUND
        elif target > nums[shifted_index(right, shift)]:
            return NOT_FOUND
        elif nums[shifted_index(right, shift)] == target:
            return shifted_index(right, shift)

        mid = 0
        while (right - left) > 1:
            mid = (right + left) // 2
            if target < nums[shifted_index(mid, shift)]:
                right = mid
            else:
                left = mid
        if nums[shifted_index(left, shift)] == target:
            return shifted_index(left, shift)
        else:
            return NOT_FOUND


# @lc code=end
