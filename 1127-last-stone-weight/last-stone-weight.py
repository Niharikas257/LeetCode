class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # maxheap = [-stone for stone in stones]
        # heapq.heapify(maxheap)

        # while len(maxheap)>1:
        #     x = -heapq.heappop(maxheap)
        #     y = - heapq.heappop(maxheap)
        #     if x != y:
        #         heapq.heappush(maxheap, -(x-y))
        # return -maxheap[0] if maxheap else 0
        if stones is None:
            return 0
        maxheap = [-stone for stone in stones]
        heapq.heapify(maxheap)
        while len(maxheap)>1:
            y = -heapq.heappop(maxheap)
            x = -heapq.heappop(maxheap)

            if x != y:
                heapq.heappush(maxheap, -(y-x))
        return -maxheap[0] if maxheap else 0
        
