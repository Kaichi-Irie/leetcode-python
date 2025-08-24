#
# @lc app=leetcode id=252 lang=python3
#
# [252] Meeting Rooms
#


# @lc code=start
class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort()
        previous_end_time = 0
        for start_time, end_time in intervals:
            if start_time < previous_end_time:
                return False
            previous_end_time = end_time
        return True


# @lc code=end
