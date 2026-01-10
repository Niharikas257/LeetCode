from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:x[0]-x[1])
        n = len(costs)//2

        total = 0
        for i in range(n):
            total += costs[i][0]

        for i in range(n, 2*n):
            total += costs[i][1]
        return total
        # n = len(costs) // 2

        # a = []  # store indices we tentatively send to A
        # b = []  # store indices we tentatively send to B

        # for i, (acost, bcost) in enumerate(costs):
        #     if acost < bcost:
        #         a.append(i)
        #     elif acost > bcost:
        #         b.append(i)
        #     else:
        #         # tie: put into the smaller side for now
        #         if len(a) <= len(b):
        #             a.append(i)
        #         else:
        #             b.append(i)

        # # If one side has more than n, move the cheapest-to-move people to the other side
        # # "Cheapest to move" means smallest penalty for switching cities.

        # if len(a) > n:
        #     # Move (len(a)-n) people from A -> B with smallest (bcost - acost)
        #     overflow = len(a) - n
        #     a.sort(key=lambda i: costs[i][1] - costs[i][0])  # smaller penalty first
        #     move = a[:overflow]
        #     keep = a[overflow:]
        #     b.extend(move)
        #     a = keep

        # elif len(b) > n:
        #     # Move (len(b)-n) people from B -> A with smallest (acost - bcost)
        #     overflow = len(b) - n
        #     b.sort(key=lambda i: costs[i][0] - costs[i][1])  # smaller penalty first
        #     move = b[:overflow]
        #     keep = b[overflow:]
        #     a.extend(move)
        #     b = keep

        # # Now both must be exactly n
        # total = 0
        # for i in a:
        #     total += costs[i][0]
        # for i in b:
        #     total += costs[i][1]

        # return total

#----------
# Find the difference between the costs from A to B and sort them, if the sum is negative, means A is cheaper, and sum is positive, B is cheaper. if all are negative, and when we sort them then we just add top n in a and next n in b, because if the difference is increasing in the negative means, the absolute value of the first number after sorting is much bigger, meaning B is very much bigger than A, so put in A



