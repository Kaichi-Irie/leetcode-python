#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#

# @lc code=start
from heapq import heappush, heappop

class Solution:
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        heap = [] # min heap
        smallest_sum_k_pairs = []

        sum_value = nums1[0] + nums2[0]
        heappush(heap, (sum_value, 0, 0))
        seen_indices = {(0, 0)}

        while heap and len(smallest_sum_k_pairs) < k:
            sum_value, index1, index2 = heappop(heap)
            smallest_sum_k_pairs.append([index1, index2])

            if index1 < len(nums1) -1 and (index1+1, index2) not in seen_indices:
                sum_value = nums1[index1+1] + nums2[index2]
                heappush(heap, (sum_value, index1+1, index2))
                seen_indices.add((index1+1, index2))
            if index2 < len(nums2) -1 and (index1, index2+1) not in seen_indices:
                sum_value = nums1[index1] + nums2[index2+1]
                heappush(heap, (sum_value, index1, index2+1))
                seen_indices.add((index1, index2+1))

        return smallest_sum_k_pairs

# @lc code=end
