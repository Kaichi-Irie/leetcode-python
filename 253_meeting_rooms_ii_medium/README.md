# 問題へのリンク
[253. Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)

# 言語
Python

# 問題の概要

会議室のスケジュールを管理するために、最小限の会議室を確保するとき、いくつの会議室が必要かを求める問題。各会議は開始時刻と終了時刻で表され、すべての会議が重複しないように会議室を割り当てる必要がある。

# 自分の解法

## step1

```python
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
```


- 時間計算量：`O(n log n)`
- 空間計算量：`O(n)`

## step2

```python
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
```

- `heappush`と`heappop`を使用する代わりに`heapreplace`を使用することで、ヒープの操作を効率化＆コードが明快に。
    - なぜ効率的か？
    - `heappop`はヒープの最小要素を削除したあと、ヒープの最後の要素を根に移動し、ヒープ木を再構築する
    - `heappush`も新しい要素を追加したあと、ヒープ木を再構築する
    - `heapreplace`は最小要素を削除して新しい要素を追加する操作を1回で行うため、効率的である。


## step3

## step4 (FB)



# 別解・模範解答

## Timeline Sweep

```python
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
```


- 時間計算量：`O(n log n)`
- 空間計算量：`O(n)`

## Two Pointers

```python
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
```

- LeetCodeに掲載されている模範解答。しかしTimeline Sweepの方がコードが明快で理解しやすいと感じた。
- 時間計算量：`O(n log n)`
- 空間計算量：`O(n)`

# 次に解く問題の予告
- [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)
