class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 # minimum speed with which koko can eat banana, it can not be zero.
        r = max(piles) # maximum probable value for the speed

        res = r # speed; this is the upper bound and will always work, but we will try for lower value
        
        while l <= r:
            k = (l+r)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
                
            if hours <= h:
                res = min(res,k)
                r = k -1
            else:
                l = k + 1
        return res
                

                



            
            


        