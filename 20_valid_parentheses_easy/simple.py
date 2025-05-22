#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
from collections import deque


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:

        PAR_L, PAR_R = "(", ")"
        BRACE_L, BRACE_R = "{", "}"
        SQBRACE_L, SQBRACE_R = "[", "]"
        stack = deque()
        for char in s:
            if char == PAR_L:
                stack.append(PAR_R)
            elif char == BRACE_L:
                stack.append(BRACE_R)
            elif char == SQBRACE_L:
                stack.append(SQBRACE_R)
            elif len(stack) == 0 or char != stack.pop():
                return False
        return len(stack) == 0


# @lc code=end
