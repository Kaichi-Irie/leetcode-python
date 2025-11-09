#
# @lc app=leetcode id=276 lang=python3
#
# [276] Paint Fence
#


# @lc code=start


def cache(function):
    """
    my implementation of functools.cache
    """
    results_cache = {}

    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs)))
        if key in results_cache:
            return results_cache[key]
        result = function(*args, **kwargs)
        results_cache[key] = result
        return result

    return wrapper


class Solution:
    @cache
    def numWays(self, n: int, k: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return k
        if n == 2:
            return k * k
        return (k - 1) * (self.numWays(n - 1, k) + self.numWays(n - 2, k))


# @lc code=end
