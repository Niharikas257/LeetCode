class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladder_jumps = []

        for i in range(len(heights) - 1):
            diff = heights[i+1] - heights[i]
            if diff <= 0:
                continue

            heapq.heappush(ladder_jumps, diff)

            if len(ladder_jumps) > ladders:
                smallest_climb_so_far = heapq.heappop(ladder_jumps)
                bricks -= smallest_climb_so_far

                if bricks < 0:
                    return i
        return len(heights) -1 
