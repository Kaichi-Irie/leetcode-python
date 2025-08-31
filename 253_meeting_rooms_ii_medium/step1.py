#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#


# @lc code=start
from heapq import heappop, heappush


class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort()
        start, end = intervals[0]
        room_end_times: list[int] = [end]
        for i, (start, end) in enumerate(intervals):
            if i == 0:
                continue
            earliest_end = room_end_times[0]
            # insert a new interval into existing room if available
            if earliest_end <= start:
                heappush(room_end_times, end)
                heappop(room_end_times)  # remove previous endtime
            else:
                # if not available, then a new room is required
                heappush(room_end_times, end)

        return len(room_end_times)


# @lc code=end
