class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        if not intervals:
            return []
        if not queries:
            return []

        intervals.sort(key=lambda x:x[0])
        sorted_query = sorted((q,idx) for idx,q in enumerate(queries))

        minheap = []
        result = [-1]*len(queries)

        n = len(intervals)
        i = 0

        for q,qi in sorted_query:
            while i < n and intervals[i][0] <= q:
                start, end = intervals[i]
                length = end-start+1
                heapq.heappush(minheap, (length, end))
                i += 1
            
            while minheap and minheap[0][1] < q:
                heapq.heappop(minheap)
            
            if minheap:
                result[qi] = minheap[0][0]
        return result

        