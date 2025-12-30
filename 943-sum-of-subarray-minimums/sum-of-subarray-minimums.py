class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        stack = []
        left = [0]*n
        right = [0]*n

        for i in range(n):
            while stack and arr[stack[-1]]>arr[i]:
                stack.pop()
            if stack:
                prev_smaller_index = stack[-1]
            else:
                prev_smaller_index = -1
            left[i] = i - prev_smaller_index 
            stack.append(i)
        stack = []

        for i in range(n-1, -1,-1):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if stack:
                next_smaller_index = stack[-1]
            else:
                next_smaller_index = n
            right[i] = next_smaller_index - i
            stack.append(i)
        
        total = 0
        for i in range(n):
            total += arr[i]*left[i]*right[i]
            total %= MOD
        return total % MOD
        

        