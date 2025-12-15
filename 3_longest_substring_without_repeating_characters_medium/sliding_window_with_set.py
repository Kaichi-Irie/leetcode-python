#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_chars: set[str] = set()
        max_length = 0
        left_index = 0
        for right_index, char in enumerate(s):
            while char in window_chars:
                window_chars.remove(s[left_index])  # O(1) on average
                left_index += 1
            window_chars.add(char)
            max_length = max(max_length, right_index - left_index + 1)

        return max_length


# @lc code=end
