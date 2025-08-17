#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Compute x to the power of n using doubling.
        Example: x=2.0, n = 10
        n = 2^3 + 2^1
        x^n = x^(2^3) * x^(2^1)

        Each x^(2^k) can be computed recursively;
        x^(2^(k+1)) = x^(2*2^k) = x^(2^k) * x^(2^k)
        """
        if n == 0:
            return 1.0
        if x == 0.0:
            return 0.0
        if n < 0:
            # x^(-n) = (1/x)^n = 1/(x^n) (n>0)
            return 1 / self.myPow(x, -n)
        x_to_power_of_two = x  # x^(2^0)
        x_to_n = 1.0  # x^n
        while n > 0:
            if n % 2 == 1:
                x_to_n *= x_to_power_of_two

            # x^(2^(k+1)) = x^(2*2^k) = x^(2^k) * x^(2^k)
            x_to_power_of_two = x_to_power_of_two * x_to_power_of_two
            n //= 2
        return x_to_n


# @lc code=end
