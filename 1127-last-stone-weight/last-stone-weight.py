class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        maxheap = [-stone for stone in stones]
        heapq.heapify(maxheap)
        res = 0

        while len(maxheap) >1:
            x = -heapq.heappop(maxheap)
            y = -heapq.heappop(maxheap)
            # if x == y:
            #     continue
                
            if x!= y:
                heapq.heappush(maxheap, -(x-y))
                
        return -maxheap[0] if maxheap else 0

        