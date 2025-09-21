#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # find the number of pairs of (i,j) s.t. 0<=i<j<=n and k = sum(nums[:j]) - sum(nums[:i])
        num_subarrays = 0
        cumsum_counts: dict[int, int] = defaultdict(int)
        cumsum = 0
        cumsum_counts[cumsum] = 1
        for num in nums:
            cumsum += num
            num_subarrays += cumsum_counts[cumsum - k]
            cumsum_counts[cumsum] += 1
        return num_subarrays


# @lc code=end
