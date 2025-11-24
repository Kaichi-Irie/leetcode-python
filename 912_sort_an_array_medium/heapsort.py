#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start
import math


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def left(index):
            return 2*index + 1
        def right(index):
            return 2*index + 2
        def parent(index):
            if index == 0:
                return 0
            return (index-1)//2

        def swap(heap, i, j):
            heap[i], heap[j] = heap[j], heap[i]

        def heappop(heap) -> int:
            if not heap:
                raise ValueError
            if len(heap) == 1:
                return heap.pop()
            min_num = heap[0]
            # heapify the remaining array
            heap[0] = heap.pop()
            index = 0
            while index < len(heap):
                min_index = index
                if left(index) < len(heap) and heap[left(index)] < heap[min_index]:
                    min_index = left(index)
                if right(index) < len(heap) and heap[right(index)] < heap[min_index]:
                    min_index = right(index)

                if min_index == index:
                    break
                swap(heap, index, min_index)
                index = min_index

            return min_num

        def heappush(heap, num):
            heap.append(num)
            index = len(heap) - 1
            while index > 0:
                if heap[index] >= heap[parent(index)]:
                    return
                swap(heap, index, parent(index))
                index = parent(index)

        heap = [] # min heap
        for num in nums:
            heappush(heap, num)
        sorted_nums = []
        while heap:
            num = heappop(heap)
            sorted_nums.append(num)
        return sorted_nums

# @lc code=end
