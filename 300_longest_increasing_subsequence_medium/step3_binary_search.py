#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start


class Solution:
    def bisect_left(self, nums: list[int], target: int) -> int:
        if not nums:
            return 0
        left = -1
        right = len(nums)
        while right - left > 1:
            mid = (right + left) // 2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid
        return right

    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0
        tails = []
        for num in nums:
            index = self.bisect_left(tails, num)
            if index == len(tails):
                tails.append(num)
                continue
            tails[index] = num
        return len(tails)


# @lc code=end
