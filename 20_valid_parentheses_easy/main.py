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

        # for c in s,
        # if c is left braces ( "(","{","[" ) : stack.push(c)
        # if c is right braces (")", "}", "]") : c_ = stack.pop(). and if c and c_ are not a pair: invalid. return False.
        def is_left(char):
            return char in [PAR_L, BRACE_L, SQBRACE_L]

        def is_right(char):
            return char in [PAR_R, BRACE_R, SQBRACE_R]

        def is_pair(char1, char2):
            S = set([char1, char2])
            return (
                S == set([PAR_L, PAR_R])
                or S == set([BRACE_L, BRACE_R])
                or S == set([SQBRACE_L, SQBRACE_R])
            )

        for char in s:
            if is_left(char):
                stack.append(char)
            elif is_right(char):
                if len(stack) == 0:
                    return False
                expected_to_be_pair = stack.pop()
                if not is_pair(char, expected_to_be_pair):
                    return False
        return len(stack) == 0


# @lc code=end
