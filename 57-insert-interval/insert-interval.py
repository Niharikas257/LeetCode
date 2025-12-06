class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res =[]
        for i in range(len(intervals)):
            old_start, old_end = intervals[i]
            if old_end < newInterval[0]:
                res.append(intervals[i])
            elif newInterval[1] < old_start:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval = [
                    min(old_start, newInterval[0]),
                    max(old_end, newInterval[1])
                ]
        res.append(newInterval)
        return res