class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return 
        next_greater = {}
        smaller = 0
        
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                smaller  = stack.pop()
                next_greater[smaller] = num
            stack.append(num)
        while stack:
            next_greater[stack.pop()] = -1
        
        return [next_greater[num] for num in nums1]
        