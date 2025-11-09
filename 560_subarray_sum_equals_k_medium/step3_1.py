#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        """
        Find the number of pairs (i,j) such that sum(nums[i:j]) == k (0<=i<j<=n).
        This can be found as below:
        for each j = 1, ..., len(nums), find the number of i (0<=i<j) that satisifes nums[:j] -k == nums[:i].
        Note that nums[:0] is defined as 0.
        """
        num_subarrays = 0
        # sum(nums[:i]) -> count
        subarray_sum_count: dict[int, int] = defaultdict(int)
        sum_to_j = 0
        # Add sum(nums[:0]) = 0
        subarray_sum_count[0] = 1
        for j in range(1, len(nums) + 1):
            sum_to_j += nums[j - 1]  # sum(nums[:j])
            count = subarray_sum_count[sum_to_j - k]
            num_subarrays += count
            subarray_sum_count[sum_to_j] += 1
        return num_subarrays


# @lc code=end
