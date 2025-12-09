class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n < 0:
            return 1.0 / self.myPow(x, -n)
        if n == 0:
            return 1
        half = self.myPow(x, n//2)

        if n%2==0:
            return half * half
        else:
            return half*half*x
        