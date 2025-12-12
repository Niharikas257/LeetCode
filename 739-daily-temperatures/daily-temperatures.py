class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        for ind, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                popped_temp, popped_ind = stack.pop()
                answer[popped_ind] = ind - popped_ind
            stack.append((temp, ind))
        return answer

        # Imagine this like a heavy temperature can compress the lower one. so whenever there is a higher temperature you pop the items before actually pushing the value on the stack. This was, the stack would be monotonically increasing.




