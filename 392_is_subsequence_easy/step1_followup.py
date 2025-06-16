#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#


# @lc code=start
from collections import defaultdict
from bisect import bisect_left


class Solution:
    # TC: O(len(s)+len(t)), but good for many s strings
    # SC: O(len(t))
    def isSubsequence(self, s: str, t: str) -> bool:
        self.set_t_cache(t)
        return self.is_subsequence_with_t_cache(s)

    def set_t_cache(self, t: str) -> None:
        char_to_indices_map: dict[str, list[int]] = defaultdict(list)
        for idx, char in enumerate(t):
            char_to_indices_map[char].append(idx)
        self.t = t
        self.char_to_indices_map = char_to_indices_map

    def is_subsequence_with_t_cache(self, s: str):
        """
        TC: O(len(s)+log(len(t)))
        """
        t = self.t
        char_to_indices_map = self.char_to_indices_map
        if t is None or char_to_indices_map is None:
            raise ValueError()
        if not s:
            return True
        elif not t or len(s) > len(t):
            return False
        # transpose hash map for string t
        # char -> indices
        last_used_index_of_t = -1
        for char in s:
            if last_used_index_of_t >= len(t):
                return False
            if char not in char_to_indices_map:
                return False
            indices = char_to_indices_map[char]
            index_of_index = bisect_left(indices, last_used_index_of_t + 1)
            # index after last_used_index_of_t was not found
            if index_of_index == len(indices):
                return False
            last_used_index_of_t = indices[index_of_index]
        return True


# @lc code=end
