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

        def can_ship(capacity: int) -> bool:
            if max(weights) > capacity:
                return False
            current_weight = 0
            days_required = 1
            for weight in weights:
                if current_weight + weight > capacity:
                    current_weight = 0
                    days_required += 1
                current_weight += weight
            return days_required <= days

        # max weight <= capacity <= sum weights
        left = 0
        right = sum(weights)
        while right - left > 1:
            mid = (right + left) // 2
            if can_ship(mid):
                right = mid
            else:
                left = mid
        return right


# @lc code=end
