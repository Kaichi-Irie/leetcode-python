#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        num_subarrays = 0
        prefix_sum_counts = defaultdict(int)
        prefix_sum = 0
        for index in range(len(nums)+1):
            if index > 0:
                prefix_sum += nums[index-1]
            count_end_with_index = prefix_sum_counts[prefix_sum-k]
            num_subarrays += count_end_with_index
            prefix_sum_counts[prefix_sum] += 1

        return num_subarrays

# @lc code=end
