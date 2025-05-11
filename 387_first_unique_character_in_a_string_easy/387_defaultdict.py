#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_cnts = defaultdict(int)
        for c in s:
            char_cnts[c] += 1

        for i, c in enumerate(s):
            if char_cnts[c] == 1:
                return i

        return -1


# @lc code=end
