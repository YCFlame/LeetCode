class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if len(intervals) < 2:
            return True
        
        intervals.sort(key=lambda x:x[0])
        start, end = intervals[0]
        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if end > s:
                return False
            
            start, end = s, e
        
        return True
