#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        num_subarrays = 0
        for i in range(len(nums)):
            subarray_sum = 0  # sum(nums[i:j+1])
            for j in range(i, len(nums)):
                subarray_sum += nums[j]
                if subarray_sum == k:
                    num_subarrays += 1
        return num_subarrays


# @lc code=end
