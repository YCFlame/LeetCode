class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        from heapq import heappush, heappop
        # The heap initialization
        end_times = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key=lambda x: x[0])

        # Add the first meeting. We have to give a new room to the first meeting.
        heappush(end_times, intervals[0][1])

        # For all the remaining meeting rooms
        for i in range(1, len(intervals)):

            # If the room due to free up the earliest is free, assign that room to this meeting.
            if end_times[0] <= intervals[i][0]:
                heappop(end_times)

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heappush(end_times, intervals[i][1])

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(end_times)
