#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
from collections import defaultdict
from heapq import heappop, heappush

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        heap = [] # min heap

        for num, count in counts.items():
            heappush(heap, (-count, num))

        topk_frequent_elements = []
        for _ in range(k):
            _, num = heappop(heap)
            topk_frequent_elements.append(num)

        return topk_frequent_elements

# @lc code=end
