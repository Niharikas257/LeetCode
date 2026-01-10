class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        cur_start, cur_end = intervals[0]
        res = []

        for i in range(1, len(intervals)):
            new_start, new_end = intervals[i]
            if new_start <= cur_end:
                cur_end = max(new_end, cur_end)
            else:
                res.append([cur_start, cur_end])
                cur_start, cur_end = new_start, new_end
        res.append([cur_start, cur_end])
        return res
