#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#


# @lc code=start
from collections import defaultdict


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        count_set = defaultdict(int)
        for num in nums:
            if count_set[num] >= 3:
                continue
            count_set[num] += 1

        nums = []
        for num, cnt in count_set.items():
            for _ in range(cnt):
                nums.append(num)

        # result: set
        # i = 0, ..., n-3
        # j = i+1, i+2, ...
        # k = n-1, n-2, ...
        # if n_i+n_j+n_k=0, then results.add(sorted(n_i,n_j,n_k))
        # if n_i+n_j+n_k > 0, then j+=1
        # if n_i+n_j+n_k < 0, then k-=1
        result = set()
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            assert 0 <= i < j < k < len(nums)
            while j < k:
                target = nums[i] + nums[j] + nums[k]
                if target == 0:
                    triplet = sorted([nums[i], nums[j], nums[k]])
                    triplet = tuple(triplet)
                    result.add(triplet)
                    j += 1
                elif target > 0:
                    k -= 1
                else:
                    j += 1
        return list(result)


# @lc code=end
