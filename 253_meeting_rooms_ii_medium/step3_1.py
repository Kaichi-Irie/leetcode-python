#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#

# @lc code=start
class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        time_events = []
        # END must comes first when time_events is sorted.
        START = 1
        END = 0
        for start_time, end_time in intervals:
            time_events.append((start_time, START))
            time_events.append((end_time, END))
        time_events.sort()
        num_rooms = 0
        max_num_rooms = 0
        for _, event_type in time_events:
            if event_type == END:
                num_rooms -= 1
            else:  # START
                num_rooms += 1
            max_num_rooms = max(max_num_rooms, num_rooms)
        return max_num_rooms


# @lc code=end
