#
# @lc app=leetcode id=252 lang=python3
#
# [252] Meeting Rooms
#


# @lc code=start
TIME_POINT_START = 1
TIME_POINT_END = -1


class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        time_points: list[tuple[int, int]] = []
        for start_time, end_time in intervals:
            time_points.append((start_time, TIME_POINT_START))
            time_points.append((end_time, TIME_POINT_END))

        time_points.sort()
        # time_points must have start time and end time in alternating order after sorting
        # if not, then there are overlapping intervals
        previous_time_type = TIME_POINT_END
        for _, time_type in time_points:
            if time_type == previous_time_type:
                return False
            previous_time_type = time_type
        return True


# @lc code=end
