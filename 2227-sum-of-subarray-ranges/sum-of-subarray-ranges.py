class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        leftMin = [0] * n
        rightMin = [0] * n
        leftMax = [0] * n
        rightMax = [0] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()
            
            if stack:
                prev_smaller_index = stack[-1]
            else:
                prev_smaller_index = -1

            leftMin[i] = i - prev_smaller_index
            
            stack.append(i)
#-----------------------------------------------------
        stack = []
        for i in range(n-1,-1,-1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            
            if stack:
                next_smaller_index = stack[-1]
            else:
                next_smaller_index = n
            
            rightMin[i] = next_smaller_index - i
            
            stack.append(i)
#-----------------------------------------------------
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            
            if stack:
                prev_larger_index = stack[-1]
            else:
                prev_larger_index = -1

            leftMax[i] = i - prev_larger_index
            
            stack.append(i)
#-----------------------------------------------------
        stack = []
        for i in range(n-1,-1,-1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            
            if stack:
                next_larger_index = stack[-1]
            else:
                next_larger_index = n

            rightMax[i] = next_larger_index - i
            
            stack.append(i)
#-----------------------------------------------------
        result = 0
        for i in range(n):
            max_contribution = nums[i] * leftMax[i] * rightMax[i]
            min_contribution = nums[i] * leftMin[i] * rightMin[i]
            result += max_contribution - min_contribution
        
        return result

        