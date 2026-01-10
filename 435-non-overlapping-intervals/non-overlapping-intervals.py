class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # intervals.sort(key = lambda x:x[1])
        # overlap = 0
        # # no_overlap = 1 # because you can always pick one interval as an answer even if all the intervals overlap.
        # old_end = intervals[0][1]

        # for i in range(1, len(intervals)):
        #     new_start, new_end = intervals[i]

        #     if old_end > new_start:
        #         overlap += 1
        #     else:
        #         # new_start >= old_end
        #         # no_overlap += 1
        #         old_end = new_end
        
        # return overlap

        if not intervals:
            return 0
        intervals.sort(key=lambda x:x[1]) # sort by end time so we have more scope to add intervals
        removals = 0

        current_start = intervals[0][0]
        current_end = intervals[0][1]

        for new_start, new_end in intervals[1:]:
            if new_start < current_end:
                removals += 1
            else:
                 current_end = new_end
        return removals
        

        
