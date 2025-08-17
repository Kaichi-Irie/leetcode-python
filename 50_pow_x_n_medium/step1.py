#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start


class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Compute x to the power of n based on these four facts;
        - x^(-n) = (1/x)^n (n>0)
        - x^0 = 1
        - x^1 = x
        - if n = 2*q + r, then x^(n) = (x^q)^2 * (x)^r

        """
        if n < 0:
            return self.myPow(1 / x, -n)
        if n == 0:
            return 1.0
        if n == 1:
            return x
        quotient, remainder = n // 2, n % 2

        return self.myPow(x, quotient) ** 2 * self.myPow(x, remainder)


# @lc code=end
