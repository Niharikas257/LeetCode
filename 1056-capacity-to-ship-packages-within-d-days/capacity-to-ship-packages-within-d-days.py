class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity):
            current_load = 0
            days_used = 1
            for weight in weights:
                if weight > capacity:
                    return False
                if current_load + weight > capacity:
                    days_used += 1
                    current_load = weight
                    if days_used > days:
                        return False
                else:
                    current_load += weight
            return True
        low = min(weights)
        high = sum(weights)
        while low < high:
            mid = low +(high - low) // 2

            if can_ship(mid):
                high = mid
            else:
                low = mid+1
        return low
        