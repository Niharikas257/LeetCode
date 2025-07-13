class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # res = []
        # subset = []
        # nums.sort()
        # seen =[]
        # def backtrack(i):
        #     if i >= len(nums):
        #         t = tuple(subset)
        #         if t not in seen:

        #             res.append(subset.copy())
        #             seen.append(t)
        #         return
            
        #     subset.append(nums[i])
        #     backtrack(i+1)
        #     subset.pop()
        #     backtrack(i+1)    
            
        # backtrack(0)
        # return res




        # res = []
        # subset = []
        # nums.sort()
        # def backtrack(start):
        #     res.append(subset.copy())
        #     for i in range(start, len(nums)):
        #         if i > start and nums[i] == nums[i-1]:
        #             continue
        #         subset.append(nums[i])
        #         backtrack(i+1)
        #         subset.pop()
        # backtrack(0)
        # return res
        

        res = []
        subset = []
        nums.sort()
        def backtrack(start):
            res.append(subset.copy())
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                subset.append(nums[i])
                backtrack(i+1)
                subset.pop()
        backtrack(0)
        return res