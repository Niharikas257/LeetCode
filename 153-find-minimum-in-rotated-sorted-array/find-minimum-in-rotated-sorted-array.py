# class Solution:
#     def findMin(self, nums: List[int]) -> int:
        
#         for i in range(len(nums) - 1):
#             if nums[i+1] < nums[i]:
#                 return nums[i+1]      
        
#         return nums[0]

class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(0, len(nums)-1):
            # j = i +1
            if nums[i+1]< nums[i]:
                return nums[i+1]
                # print('Hello')
        
        return nums[0]