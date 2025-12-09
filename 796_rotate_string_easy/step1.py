#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#

# @lc code=start
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        def is_same(string1: str, string2: str, offset: int) -> bool:
            for i in range(len(string1)):
                    if string1[i] != string2[(i+offset)%len(string2)]:
                        return False
            return True

        if len(s) != len(goal):
            return False
        if not s:
            return True
        matched_indices = [i for i in range(len(goal)) if goal[i]==s[0]]
        while matched_indices:
            offset = matched_indices.pop()
            if is_same(s, goal, offset):
                return True
        return False


# @lc code=end
