#
# @lc app=leetcode id=252 lang=python3
#
# [252] Meeting Rooms
#


# @lc code=start


class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort()
        previous_end = 0
        for start, end in intervals:
            if start < previous_end:
                return False
            previous_end = end
        return True


# @lc code=end
