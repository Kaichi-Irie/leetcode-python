#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(1 / x, -n)
        power_of_x = x
        i = 0
        two_to_i = 1
        x_to_n = 1.0
        while two_to_i <= n:
            if n >> i & 1:
                x_to_n *= power_of_x
            i += 1
            two_to_i *= 2
            power_of_x = power_of_x * power_of_x
        return x_to_n


# @lc code=end
