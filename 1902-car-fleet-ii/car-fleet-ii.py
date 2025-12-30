class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        from typing import List
        n = len(cars)
        ans = [-1.0] * n
        stack: List[int] = []
        for i in range(n - 1, -1, -1):
            pos_i, speed_i = cars[i]
            while stack:
                j = stack[-1]
                pos_j, speed_j = cars[j]
                if speed_i <= speed_j: # they will not collide
                    stack.pop()
                    continue
                t = (pos_j - pos_i) / (speed_i - speed_j) # they do collide, or car i is faster
                if ans[j] < 0 or t <= ans[j] + 1e-12: # if j has not collided with anyone so it will definitely collide with i and the time of i should be less than j
                    ans[i] = t
                    break
                stack.pop()
            stack.append(i)

        return ans


        
        