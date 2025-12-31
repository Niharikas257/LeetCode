class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 0
        high = num
        while low <= high:
            mid = low + (high - low) // 2
            res = mid * mid
            if res < num:
                low = mid + 1
            elif res > num:
                high = mid - 1
            else:
                return True
        return False
