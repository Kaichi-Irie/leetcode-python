#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#
# @lc code=start
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        """
        Find the subarraySum in O(n) when nums have positive elements.
        """
        if not nums:
            return 0
        num_subarrays = 0
        subarray_sum = 0
        left = 0
        for right in range(len(nums)):
            subarray_sum += nums[right]
            while left < right and subarray_sum > k:
                subarray_sum -= nums[left]
                left += 1

            if subarray_sum == k:
                num_subarrays += 1

        return num_subarrays


# @lc code=end
