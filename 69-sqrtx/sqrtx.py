class Solution:
    def mySqrt(self, x: int) -> int:
        low = 1
        high = x
        ans = 1
        if x < 2:
            return x
        while low <= high:
            mid = low + (high-low)//2
            res = mid * mid
            if res <= x:
                ans = mid
                low = mid+ 1
            else:
                high = mid - 1
        return ans
        