class Solution:
    def containsDuplicate(self, nums: List[int])-> bool:
        res = set()
        for i in range(len(nums)):
            res.add(nums[i])
        
        if len(res) == len(nums):
            return False
        
        return True
        # res = set()
        # for i in range(len(nums)):
        #     if nums[i] in res:
        #         return True
        #     else:
        #         res.add(nums[i])
        # return False

# class Solution:
#     def containsDuplicate(self, nums: List[int])-> bool:
#         nums.sort()
#         for i in range(len(nums)-1):
#             if nums[i] == nums[i+1]:
#                 return True
#         return False


        