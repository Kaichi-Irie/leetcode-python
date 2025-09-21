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
        MIN = -(2**31)
        MAX = 2**31 - 1
        if not s:
            return 0
        num = 0
        # remove leading whitespaces
        i = 0
        while i < len(s) and s[i] == SPACE:
            i += 1
        s = s[i:]
        if not s:
            return 0
        # process sign
        is_negative = False
        if s[0] == PLUS:
            s = s[1:]
        elif s[0] == MINUS:
            s = s[1:]
            is_negative = True
        if not s:
            return 0
        # conversion
        digits: list[int] = []
        for char in s:
            if char not in self.CHAR_TO_DIGIT:
                break
            digit = self.CHAR_TO_DIGIT[char]
            digits.append(digit)
        digits.reverse()
        for i, digit in enumerate(digits):
            num += digit * pow(10, i)
        num = -num if is_negative else num
        # rounding
        num = min(num, MAX)
        num = max(num, MIN)

        return num


# @lc code=end
