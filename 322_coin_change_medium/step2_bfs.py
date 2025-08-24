#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
from collections import deque


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        Solves the coin change problem by treating it as a shortest path problem on a graph. Each amount is a node, and each coin represents an edge.

        This implementation uses Breadth-First Search (BFS) to find the shortest path from the `amount` node to the `0` node. The length of this path corresponds to the minimum number of coins required.
        """
        queue = deque([(amount, 0)])
        visited: set[int] = {amount}
        while queue:
            current_amount, num_coins = queue.popleft()
            if current_amount == 0:
                return num_coins
            for coin in coins:
                if current_amount < coin:
                    continue
                next_amount = current_amount - coin
                if next_amount not in visited:
                    visited.add(next_amount)
                    queue.append((next_amount, num_coins + 1))
        # cannot change
        return -1


# @lc code=end
