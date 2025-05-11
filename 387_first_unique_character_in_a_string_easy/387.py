#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_cnts = {}
        for c in s:
            if c in char_cnts:
                char_cnts[c] += 1
            else:
                char_cnts[c] = 1

        for i, c in enumerate(s):
            if char_cnts[c] == 1:
                return i

        return -1


# @lc code=end
