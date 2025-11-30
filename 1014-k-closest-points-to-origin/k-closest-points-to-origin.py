class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for (x,y) in points:
            dist = x*x + y*y
            heapq.heappush(minheap, (dist,x,y))
        
        heapq.heapify(minheap)

        res = []
        while len(res)< k:
            _, x, y = heapq.heappop(minheap)
            res.append([x,y])
        return res


        