class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x[1]) # sort by end time so we have more scope to add intervals
        removals = 0

        current_start = intervals[0][0]
        current_end = intervals[0][1]

        for new_start, new_end in intervals[1:]:
            if new_start < current_end: # Usually closed brackets are <= (overlapping) but it is mentioned that they are not, so we should consider them as open bracket.
                removals += 1
            else:
                 current_end = new_end
        return removals
        

        
