#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # character -> last index
        char_to_last_index: dict[str, int] = defaultdict(int)

        # window manages the trailing substring
        window_start_index = 0
        max_length = 0
        for index, char in enumerate(s):
            if char in char_to_last_index:
                window_start_index = max(
                    window_start_index, char_to_last_index[char] + 1
                )
            max_length = max(max_length, index - window_start_index + 1)
            char_to_last_index[char] = index
        return max_length


# @lc code=end
