#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if x == 0.0:
            return 0.0
        if n == 1:
            return x
        if n < 0:
            n = -n
            x = 1 / x
            return self.myPow(x, n)

        half_n = n // 2
        remainder = n % 2

        return self.myPow(x, half_n) ** 2 * self.myPow(x, remainder)


# @lc code=end
