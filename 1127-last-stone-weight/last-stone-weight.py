import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # # Simulate a max heap by negating all the values
        # stones = [-s for s in stones]
        # heapq.heapify(stones)

        # while len(stones) > 1:
        #     # Get two heaviest stones
        #     first = -heapq.heappop(stones)
        #     second = -heapq.heappop(stones)
            
        #     if first != second:
        #         # Push the difference back into heap
        #         heapq.heappush(stones, -(first - second))

        # # Return the last remaining stone or 0
        # return -stones[0] if stones else 0
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)

            if x != y:
                heapq.heappush(stones, (y-x))

        return -stones[0] if stones else 0
