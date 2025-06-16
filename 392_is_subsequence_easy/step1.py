#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#


# @lc code=start
class Solution:
    # TC: O(len(s)+len(t))
    # SC: O(1)
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        elif not t or len(s) > len(t):
            return False
        i = 0
        j = 0
        while i < len(s):
            if j >= len(t):
                return False
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

        return True


# @lc code=end
