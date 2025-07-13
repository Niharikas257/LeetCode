class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()
        seen =[]
        def backtrack(i):
            if i >= len(nums):
                t = tuple(subset)
                if t not in seen:

                    res.append(subset.copy())
                    seen.append(t)
                return
            
            subset.append(nums[i])
            backtrack(i+1)
            subset.pop()
            # while i+1 < len(nums) and nums[i] == nums[i+1]:
            #     i+=1 # skip the element is the elements are same
            backtrack(i+1)    
            
        backtrack(0)
        return res
        