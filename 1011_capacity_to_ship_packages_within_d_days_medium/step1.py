#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        if not weights:
            return 0

        def can_ship_within_days(days: int, capacity: int) -> bool:
            cargo_weight = 0
            days_required = 1
            for weight in weights:
                if weight > capacity:
                    return False
                if cargo_weight + weight > capacity:
                    cargo_weight = 0
                    days_required += 1
                cargo_weight += weight
            return days_required <= days

        # 0 < capacity <= sum weights
        left = 0
        right = sum(weights)
        while right - left > 1:
            mid = (right + left) // 2
            if can_ship_within_days(days, mid):
                right = mid
            else:
                left = mid
        return right


# @lc code=end
