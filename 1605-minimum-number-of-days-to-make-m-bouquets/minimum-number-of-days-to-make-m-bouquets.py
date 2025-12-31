# class Solution:
#     def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
#         if m*k > n:
#             return -1

#         left = min(bloomDay)
#         right = max(bloomDay)

#         def canMake(day):
#             consecutive = 0
#             bouquets = 0

#             for bloom in bloomDay:
#                 if bloom <= day:
#                     consecutive += 1
#                     if consecutive == k:
#                         bouquets += 1

#                         if bouquets >= m:
#                             return True
#                 else:
#                     consecutive = 0
#             return bpuquets >= m

#         while left <= right:
#             mid = (left+right) // 2
#             if canMake(mid):
#                 high = mid
#             else:
#                 low = mid + 1
#         return low


class Solution:    
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m*k > n:
            return -1

        def canMake(day):
            adjacent = 0
            bouquets = 0
            # cur_day = 0

            for bloom in bloomDay:
                if bloom <= day:
                    adjacent += 1
                    if adjacent == k:
                        bouquets += 1
                        adjacent = 0
                        if bouquets >= m:
                            return True
                else:
                    adjacent = 0
            return bouquets >= m

        left = min(bloomDay)
        right = max(bloomDay)
        while left < right:
            mid = (left+right) // 2
            if canMake(mid):
                right = mid
            else:
                left = mid + 1
        return left







