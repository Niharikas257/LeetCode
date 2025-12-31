class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        from typing import List

        position.sort()
        def can_place(dist: int) -> bool:
            count = 1
            last_pos = position[0]

            # Try to place remaining cows greedily
            for pos in position[1:]:
                if pos - last_pos >= dist:
                    count += 1
                    last_pos = pos
                    if count >= m:
                        return True

            return False

        # Binary search on the minimum distance
        low = 0
        high = position[-1] - position[0]
        best = 0

        while low <= high:
            mid = low + (high - low) // 2

            if can_place(mid):
                best = mid          # mid is feasible, save it
                low = mid + 1       # try to push distance larger
            else:
                high = mid - 1      # mid is not feasible, reduce distance

        return best

        