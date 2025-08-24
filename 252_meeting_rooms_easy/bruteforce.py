#
# @lc app=leetcode id=252 lang=python3
#
# [252] Meeting Rooms
#


# @lc code=start
class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:

        def are_overlapping(
            start_time1: int,
            end_time1: int,
            start_time2: int,
            end_time2: int,
        ) -> bool:
            if start_time1 < end_time1 <= start_time2 < end_time2:
                return False
            elif start_time2 < end_time2 <= start_time1 < end_time1:
                return False
            return True

        for i in range(len(intervals) - 1):
            for j in range(i + 1, len(intervals)):
                if are_overlapping(*intervals[i], *intervals[j]):
                    return False
        return True


# @lc code=end
