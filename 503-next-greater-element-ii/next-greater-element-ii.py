class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return 
        smaller = 0
        stack = []
        next_greater = [-1]*len(nums)
        for i in range(len(nums)*2):
            idx = i % len(nums)
            while stack and nums[stack[-1]] < nums[idx]:
                smaller = stack.pop()
                next_greater[smaller] = nums[idx]
            if i < len(nums):
                stack.append(idx)
        
        return next_greater
        