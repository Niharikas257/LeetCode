class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pair = [(p,s) for p, s in zip(position,speed)]
        # stack = []
        # # res = []

        # for p,s in sorted(pair)[::-1]:
        #     stack.append((target-p)/s)
        #     if len(stack)>=2 and stack[-1]<=stack[-2]:
        #         stack.pop()
        # return len(stack)
        
        pair = [(p,s) for p,s in zip(position,speed)]
        pair.sort(reverse=True)
        prevTime = (target-pair[0][0])/pair[0][1]
        fleet = 1

        for i in range(1, len(pair)):
            currcar = pair[i]
            currTime = (target-currcar[0])/currcar[1]
            if currTime > prevTime:
                fleet += 1
                prevTime = currTime
        return fleet


            