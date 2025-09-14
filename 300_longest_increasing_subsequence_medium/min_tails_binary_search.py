#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        def bisect_left(array: list, x: int) -> int:
            if not array:
                return 0
            if array[-1] < x:
                return len(array)
            left = -1
            right = len(array) - 1
            while right - left > 1:
                mid = (right + left) // 2
                if array[mid] >= x:
                    right = mid
                else:
                    left = mid
            return right

        if not nums:
            return 0
        min_tails = [nums[0]]
        for num in nums[1:]:
            j = bisect_left(min_tails, num)
            if j == len(min_tails):
                min_tails.append(num)
            else:
                min_tails[j] = num
        return len(min_tails)


# @lc code=end
