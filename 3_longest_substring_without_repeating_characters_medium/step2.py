#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


# @lc code=start
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        # character -> last index
        char_to_last_index: dict[str, int] = defaultdict(int)
        window_start_index = 0
        max_length = 0

        # consider two substrings at every iteration;
        # 1. trailing substring: starts at substring_start_index, ends at index, and managed by a window
        # 2. last longest substring: only length information is saved as max_length
        # at the end of every iteration, we update max_length
        for index, char in enumerate(s):
            if char in char_to_last_index:
                window_start_index = max(
                    window_start_index, char_to_last_index[char] + 1
                )
            char_to_last_index[char] = index
            max_length = max(max_length, index - window_start_index + 1)
        return max_length


# @lc code=end
