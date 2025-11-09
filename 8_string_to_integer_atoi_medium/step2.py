#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
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
        index = 0
        while index < len(s) and s[index] == SPACE:
            index += 1
        # process sign
        sign = 1
        if index < len(s) and s[index] == PLUS:
            index += 1
        elif index < len(s) and s[index] == MINUS:
            sign = -1
            index += 1
        # conversion
        while index < len(s) and "0"<=s[index]<="9":
            digit = ord(s[index]) - ord("0")
            num = num * 10 + digit
            index += 1

        num = sign * num
        # rounding
        num = min(num, MAX_INT)
        num = max(num, MIN_INT)

        return num


# @lc code=end
