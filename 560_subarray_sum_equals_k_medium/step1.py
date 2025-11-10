#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        num_subarrays = 0
        # cumsums[i] = sum(nums[:i])
        # sum(nums[i:j]) = cumsums[i] - cumsums[j]
        cumsums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            cumsums[i + 1] = cumsums[i] + nums[i]

        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                sum_from_i_to_j = cumsums[j] - cumsums[i]
                if sum_from_i_to_j == k:
                    num_subarrays += 1

        return num_subarrays


# @lc code=end
