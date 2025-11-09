#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        index = 0
        # Process whitespace
        SPACE = " "
        while index < len(s) and s[index] == SPACE:
            index += 1

        # Process signedness
        is_negative = False
        MINUS = "-"
        PLUS = "+"
        if index < len(s) and s[index] == MINUS:
            is_negative = True
            index += 1
        elif index < len(s) and s[index] == PLUS:
            index += 1

        # Process conversion
        num = 0
        # leading zeros
        while index < len(s) and s[index] == str(0):
            index += 1
        digits = [str(i) for i in range(10)]
        while index < len(s) and s[index] in digits:
            digit = int(s[index])
            num = num*10 + digit
            index += 1

        # apply signedness

        num = -num if is_negative else num

        # Process rounding
        INT_MIN = -2**31
        INT_MAX = 2**31 -1
        num = min(num, INT_MAX)
        num = max(num, INT_MIN)
        return num


# @lc code=end
