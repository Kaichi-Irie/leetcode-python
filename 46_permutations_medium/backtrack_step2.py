#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#


# @lc code=start
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        all_permutations = []
        self.backtrack(nums, [], all_permutations)
        return all_permutations

    def backtrack(
        self, remaining: list[int], chosen: list[int], all_permutations: list[list[int]]
    ) -> None:

        # If all the numbers in nums are chosen (i.e. remaining is empty), then store the chosen list in all_permutations as one possible permutation.
        if not remaining:
            all_permutations.append(chosen)

        # choose an element from remaining, and add it to chosen and call backtrack recursively.
        # e.g. remaining = [3,4], chosen = [1], then
        # call backtrack([4],[1,3])->backtrack([],[1,3,4]); all_permutations.append([1,3,4])
        # call backtrack([3],[1,4])->backtrack([],[1,4,3]); all_permutations.append([1,4,3])
        for i in range(len(remaining)):
            num = remaining[i]
            new_remaining = remaining[:i] + remaining[i + 1 :]
            new_chosen = chosen + [num]
            self.backtrack(new_remaining, new_chosen, all_permutations)


# @lc code=end
