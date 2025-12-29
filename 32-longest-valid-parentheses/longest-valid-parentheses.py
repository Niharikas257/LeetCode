class Solution:
    def longestValidParentheses(self, s: str) -> int:
        arr = []
        for ch in s:
            arr.append(ch)
        max_length = 0
        length = 0

        stack = [-1]
        for i, ch in enumerate(arr):
            if ch == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    length = i - stack[-1]
                    max_length = max(max_length, length)
        return max_length


        