class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:


        # x,y,z = target

        # have_a = have_b = have_c = False    

        # for a,b,c in triplets:
        #     if a > x or b > y or c > z:
        #         continue
            
        #     if a == x:
        #         have_a = True
        #     if b == y:
        #         have_b = True
        #     if c == z:
        #         have_c = True
        # return have_a and have_b and have_c

        x,y,z = target

        have_a = have_b = have_c = False    

        for triplet in triplets:
            if triplet[0]> x or triplet[1] > y or triplet[2] > z:
                continue
            
            if triplet[0] == x:
                have_a = True
            if triplet[1] == y:
                have_b = True
            if triplet[2] == z:
                have_c = True
        return have_a and have_b and have_c


        



        