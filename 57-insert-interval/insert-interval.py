class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # res = []
        # for i in range(len(intervals)):
        #     old_start, old_end = intervals[i]
        #     if old_end < newInterval[0]:
        #         res.append(intervals[i])
        #     elif old_start > newInterval[1]:
        #         res.append(newInterval)
        #         return res + intervals[i:]
        #     else:
        #         newInterval = [
        #             min(old_start, newInterval[0]),
        #             max(old_end, newInterval[1])
        #         ]
        # res.append(newInterval)
        # return res


        new_start = newInterval[0]
        new_end = newInterval[1]

        n = len(intervals)
        i = 0
        res = []
        while i < n and intervals[i][1] < new_start:
            res.append(intervals[i])
            i += 1
        
        while i < n and intervals[i][0] <= new_end:
            new_start = min(intervals[i][0], new_start)
            new_end = max(intervals[i][1], new_end)
            i += 1
        
        res.append([new_start, new_end])

        while i < n:
            res.append(intervals[i])
            i+=1 
        
        return res

