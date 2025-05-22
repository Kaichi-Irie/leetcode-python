#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:

        PAR_O, PAR_C = "(", ")"
        BRACE_O, BRACE_C = "{", "}"
        SQBRACE_O, SQBRACE_C = "[", "]"
        pairs = {
            PAR_O: PAR_C,
            PAR_C: PAR_O,
            BRACE_O: BRACE_C,
            BRACE_C: BRACE_O,
            SQBRACE_O: SQBRACE_C,
            SQBRACE_C: SQBRACE_O,
        }

        def is_open(brace):
            return brace in [
                PAR_O,
                BRACE_O,
                SQBRACE_O,
            ]

        def is_closed(brace):
            return brace in [
                PAR_C,
                BRACE_C,
                SQBRACE_C,
            ]

        def process(s, i):
            print(f"{i=}, {s[i]=}")
            opening = s[i]
            if not is_open(opening):
                return False, -1
            i += 1
            b, i = process(s, i)
            if b is False:
                return False, -1
            closing = s[i]
            if not is_closed(closing):
                return False, -1
            if closing != pairs[opening]:
                return False, -1
            i += 1
            return True, i

        i = 0
        while i < len(s):
            b, i = process(s, i)
            if b is False:
                return False


# @lc code=end
