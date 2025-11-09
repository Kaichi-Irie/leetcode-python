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
        substring_start_index = 0
        max_length = 0

        for index, char in enumerate(s):
            if char in char_to_last_index:
                substring_start_index = max(
                    substring_start_index, char_to_last_index[char] + 1
                )
            char_to_last_index[char] = index
            max_length = max(max_length, index - substring_start_index + 1)
        return max_length


# @lc code=end
