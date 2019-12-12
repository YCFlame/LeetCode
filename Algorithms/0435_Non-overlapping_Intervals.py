class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2:
            return 0
        
        intervals.sort()
        l, h = intervals[0]
        rs = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < h:
                rs += 1
                h = min(h, intervals[i][1])
            else:
                h = intervals[i][1]
                
        return rs
