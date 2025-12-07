#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
from functools import cache

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        @cache
        def find_combination_sum(target: int) -> set[tuple]:
            if target == 0:
                return {()}
            if target < 0:
                return set()
            combinations = set()
            for candidate in candidates:
                combination_set = find_combination_sum(target-candidate)
                for combination in combination_set:
                    combination = tuple(list(combination) + [candidate])
                    combination = tuple(sorted(combination))
                    combinations.add(combination)
            return combinations

        combinations_set = find_combination_sum(target)
        return [list(combination) for combination in combinations_set]
# @lc code=end
