from typing import List
import math

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        min_rank = min(ranks)

        # Upper bound: fastest mechanic does all cars alone
        low = 0
        high = min_rank * cars * cars

        def can_finish(T: int) -> bool:
            total = 0
            for r in ranks:
                total += math.isqrt(T // r)
                if total >= cars:
                    return True
            return False

        # Find minimum feasible time
        while low < high:
            mid = low + (high - low) // 2
            if can_finish(mid):
                high = mid
            else:
                low = mid + 1

        return low
