#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#

# @lc code=start
class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        meeting_events = []
        # meeting events will be sorted in ascending order
        # so end must come ahead
        START = 1
        END = 0
        for start_time, end_time in intervals:
            meeting_events.append((start_time, START))
            meeting_events.append((end_time, END))

        meeting_events.sort()

        max_rooms = 0
        num_rooms = 0
        for _, event_type in meeting_events:
            if event_type == START:
                num_rooms += 1
            if event_type == END:
                num_rooms -= 1
            max_rooms = max(max_rooms, num_rooms)
        return max_rooms


# @lc code=end
