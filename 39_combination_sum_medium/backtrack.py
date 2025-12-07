#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        seen = set()
        combinations: set[tuple] = set()
        def backtrack(combination: list, sum_value):
            canonical_combination = tuple(sorted(combination))
            if canonical_combination in seen:
                return
            seen.add(canonical_combination)
            if sum_value == target:
                combinations.add(canonical_combination)
                return
            for candidate in candidates:
                if sum_value + candidate > target:
                    continue
                combination.append(candidate)
                backtrack(combination, sum_value+candidate)
                combination.pop()
        backtrack([], 0)
        return [list(combination) for combination in combinations]

# @lc code=end
