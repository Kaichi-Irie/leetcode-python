#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row_to_chars = {row: [] for row in range(numRows)}
        row = 0
        down = True
        # insert chars into row_to_chars in zigzag orders
        for char in s:
            row_to_chars[row].append(char)
            if down and row == numRows - 1 :
                down = False
            elif not down and row == 0:
                down = True

            if down:
                row = min(row+1, numRows-1)
            else:
                row = max(row-1, 0)



        zigzag_chars = []
        for row in range(numRows):
            zigzag_chars.extend(row_to_chars[row])

        return "".join(zigzag_chars)
# @lc code=end
