#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#

# @lc code=start
import math


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def mergesort(start, end):
            """
            sort nums[start:end]
            """
            if end - start <= 1:
                return
            mid = (start + end) // 2
            mergesort(start, mid)
            mergesort(mid, end)

            # merge the sorted arrays, nums[start:mid] and nums[mid:end].
            sorted_nums = []
            pointer1 = start
            pointer2 = mid
            while pointer1 < mid or pointer2 < end:
                num1 = math.inf if pointer1 >= mid else nums[pointer1]
                num2 = math.inf if pointer2 >= end else nums[pointer2]

                if num1 < num2:
                    sorted_nums.append(num1)
                    pointer1 += 1
                else:
                    sorted_nums.append(num2)
                    pointer2 += 1
            nums[start:end] = sorted_nums

        mergesort(0, len(nums))
        return nums
# @lc code=end
