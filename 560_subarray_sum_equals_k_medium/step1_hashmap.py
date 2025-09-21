#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # k = nums[i:j] = cumsums[j] - cumsums[i]
        # if cumsums[j]-k in cumsum_hashmap for j in i+1, ..., then OK
        num_subarrays = 0
        # cumsums[i] = sum(nums[:i])
        cumsums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            cumsums[i + 1] = cumsums[i] + nums[i]

        hashmap: dict[int, int] = defaultdict(int)
        for i in range(len(nums) + 1):
            num_subarrays += hashmap[cumsums[i] - k]
            hashmap[cumsums[i]] += 1
        return num_subarrays


# @lc code=end
