#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#


# @lc code=start
from collections import defaultdict


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        hashmap = defaultdict(list)  # value of element->indices
        # create hashmap
        for idx, val in enumerate(nums):
            if len(hashmap[val]) > 3:
                continue
            hashmap[val].append(idx)

        # search for all the triplets
        triplets = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                num_i, num_j = nums[i], nums[j]
                key_val = -(num_i + num_j)
                if key_val in hashmap.keys():
                    for k in hashmap[key_val]:
                        if k == i or k == j:
                            continue
                        num_k = nums[k]
                        tpl = tuple(sorted([num_i, num_j, num_k]))
                        triplets.add(tpl)
                        break
        return list(triplets)


# @lc code=end
