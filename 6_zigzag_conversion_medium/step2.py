#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row_to_chars = [[] for _ in range(numRows)]
        if numRows == 1:
            return s
        backward = True
        row = 0
        for char in s:
            if row == 0 or row == numRows - 1:
                backward = not backward
            row_to_chars[row].append(char)
            if backward:
                row -= 1
            else:
                row += 1

        converted_chars = []
        for row in range(numRows):
            converted_chars.extend(row_to_chars[row])

        return "".join(converted_chars)



# @lc code=end
