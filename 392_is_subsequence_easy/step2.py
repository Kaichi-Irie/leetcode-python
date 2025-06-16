#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#


# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0
        t_pointer = 0
        while s_pointer < len(s) and t_pointer < len(t):
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
                t_pointer += 1
            else:
                t_pointer += 1

        return s_pointer == len(s)


# @lc code=end
