class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def can(P: int) -> bool:
            ops = 0
            for x in nums:
                ops += (x - 1) // P
                if ops > maxOperations:
                    return False
            return True
        low = 1
        high = max(nums)
        while low < high:
            mid = low + (high - low) // 2
            if can(mid):
                high = mid
            else:
                low = mid + 1
        return low 

        