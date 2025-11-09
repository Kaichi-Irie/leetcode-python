#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#

# @lc code=start

from heapq import heappush, heapreplace


class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort()
        start, end = intervals[0]
        meeting_end_times = []
        heappush(meeting_end_times, end)
        for start, end in intervals[1:]:
            earliest_end = meeting_end_times[0]
            # If the earliest available room is free, reuse it.
            if earliest_end <= start:
                heapreplace(meeting_end_times, end)
            # Otherwise, allocate a new room
            else:
                heappush(meeting_end_times, end)

        return len(meeting_end_times)


# @lc code=end
