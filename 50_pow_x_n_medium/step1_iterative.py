#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start


class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Compute x to the power of n by using iterative method.
        Example: x=2.0 and n = 10
        n = 2^3 + 2^1, so
        x^n = x^(2^3) * x^(2^1)
        x^1, ..., x^(2^k) can be computed in O(k) by using this formula; x^(2^(k+1)) = x^(2*2^k) = x^(2^k) * x^(2^k)
        Therefore, x^n can be also computed in O(log(n))

        Time Complexity: O(log(n))
        Space Complexity: O(1)
        """
        if x == 0.0:
            return 0.0
        if n == 0:
            return 1.0
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n == 1:
            return x

        x_to_n = 1.0  # x^n
        bit_position = 0  # k
        power_of_two = 1  # 2^k
        x_to_power_of_two = x  # x^(2^k)
        while power_of_two <= n:
            if (n >> bit_position) & 1:
                x_to_n *= x_to_power_of_two
            bit_position += 1
            x_to_power_of_two = x_to_power_of_two * x_to_power_of_two
            power_of_two = 2 * power_of_two

        return x_to_n


# @lc code=end
