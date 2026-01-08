class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [0] * len(points)
        res = []
        for i, (x,y) in enumerate(points):
            dist[i] = x*x + y*y
        minheap = []
        for i, distance in enumerate(dist):
            heapq.heappush(minheap, (distance, i))
            # if len(minheap) > k:
            #     heapq.heappop(minheap)
        res = []
        for _ in range(k):
            _, i = heapq.heappop(minheap)
            res.append(points[i])
        return res






