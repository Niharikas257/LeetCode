class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            alive = True
            while stack and alive and stack[-1] > 0 and asteroid < 0:
                top = stack[-1]
                if abs(top) < abs(asteroid):
                    stack.pop()
                elif abs(top) == abs(asteroid):
                    stack.pop()
                    alive = False
                else:
                    alive = False

            if alive:
                stack.append(asteroid)
        return stack

        