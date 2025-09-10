#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#

# @lc code=start
from heapq import heappush, heappushpop


class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort()
        num_rooms = 0
        start_time, end_time = intervals[0]
        heap = []
        heappush(heap, end_time)
        for start_time, end_time in intervals[1:]:
            earliest_end_time = heap[0]
            if start_time < earliest_end_time:
                heappush(heap, end_time)
                continue
            # use the same room after the earliest meeting ends
            heappushpop(heap, end_time)
        return len(heap)


# @lc code=end
