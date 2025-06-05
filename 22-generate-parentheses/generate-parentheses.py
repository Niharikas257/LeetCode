# from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # result = []
        # if n == 0:
        #     return [""]

        # # Each stack entry holds a tuple: (current_string, open_used, close_used)
        # stack = [("", 0, 0)]

        # while stack:
        #     curr, open_used, close_used = stack.pop()

        #     # If we've placed all 2*n parentheses, record the valid combination
        #     if open_used == n and close_used == n:
        #         result.append(curr)
        #         continue

        #     # We push next states in reverse order of how we want to explore them
        #     # because the stack is LIFO. To try "(" before ")", push ")" first.

        #     # 1) If we can still place a ")", push that option:
        #     #    valid only if close_used < open_used
        #     if close_used < open_used:
        #         stack.append((curr + ")", open_used, close_used + 1))

        #     # 2) If we can still place a "(", push that option:
        #     #    valid only if open_used < n
        #     if open_used < n:
        #         stack.append((curr + "(", open_used + 1, close_used))

        # return result
        stack = []
        res = []

        def backTrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backTrack(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                backTrack(openN, closedN +1)
                stack.pop()
            
        backTrack(0,0)
        return res

