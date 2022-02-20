class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:    
        intervals.sort(key = lambda x: x[0])        
        lastInterval = intervals[0]
        count = 1
        for i in range(1, len(intervals)):
            if intervals[i][1] <= lastInterval[1]:
                continue
            elif intervals[i][0] == lastInterval[0] and lastInterval[1] <= intervals[i][1]:
                lastInterval = intervals[i]
                continue
            lastInterval = intervals[i]
            count += 1
        return count