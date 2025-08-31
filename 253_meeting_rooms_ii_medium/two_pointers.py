#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#

# @lc code=start
class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        start_times: list[int] = [interval[0] for interval in intervals]
        end_times: list[int] = [interval[1] for interval in intervals]

        start_times.sort()
        end_times.sort()
        max_rooms = 0
        start_time_pointer = 0
        end_time_pointer = 0
        while start_time_pointer < len(intervals):
            start_time = start_times[start_time_pointer]
            end_time = end_times[end_time_pointer]
            if start_time < end_time:
                start_time_pointer += 1
            else:
                end_time_pointer += 1
            max_rooms = max(max_rooms, start_time_pointer - end_time_pointer)
        return max_rooms


# @lc code=end
