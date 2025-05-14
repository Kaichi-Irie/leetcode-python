#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#
from typing import List, Optional
from math import inf
from functools import cache
import heapq
from heapq import heappush, heappop


# @lc code=start
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort(reverse=True)
        self.nums = nums
        self.N = len(nums)
        heap = []
        for num in nums[: min(k, self.N)]:
            heappush(heap, num)
        self.heap = heap

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        while len(self.heap) > self.k:
            _ = heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end
