#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start

import bisect


class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def can_ship(capacity: int) -> bool:
            if max(weights) > capacity:
                return False
            current_weight = 0
            days_required = 1
            for weight in weights:
                current_weight += weight
                if current_weight > capacity:
                    days_required += 1
                    current_weight = weight
            return days_required <= days

        return bisect.bisect_left(range(sum(weights) + 1), True, key=can_ship)


# @lc code=end
