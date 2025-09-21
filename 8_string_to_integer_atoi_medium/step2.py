#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    CHAR_TO_DIGIT = {str(i): i for i in range(10)}

    def myAtoi(self, s: str) -> int:
        SPACE = " "
        PLUS = "+"
        MINUS = "-"
        MIN_INT = -(2**31)
        MAX_INT = 2**31 - 1

        if not s:
            return 0
        num = 0

        # remove leading whitespaces
        i = 0
        while i < len(s) and s[i] == SPACE:
            i += 1
        # process sign
        sign = 1
        if i < len(s) and s[i] == PLUS:
            i += 1
        elif i < len(s) and s[i] == MINUS:
            sign = -1
            i += 1
        # conversion
        while i < len(s) and s[i] in self.CHAR_TO_DIGIT:
            digit = self.CHAR_TO_DIGIT[s[i]]
            num = num * 10 + digit
            i += 1
        num = sign * num
        # rounding
        num = min(num, MAX_INT)
        num = max(num, MIN_INT)

        return num


# @lc code=end
