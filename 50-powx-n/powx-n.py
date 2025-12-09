class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n%2==0:
            return (x*x)**(n//2)
        else:
            return ((x*x)**(n//2)) * x
        