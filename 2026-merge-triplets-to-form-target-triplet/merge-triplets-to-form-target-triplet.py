class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:


        x,y,z = target

        have_a = have_b = have_c = False    

        for a,b,c in triplets:
            if a > x or b > y or c > z:
                continue
            
            if a == x:
                have_a = True
            if b == y:
                have_b = True
            if c == z:
                have_c = True
        return have_a and have_b and have_c


        



        