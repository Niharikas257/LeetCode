class Solution:
    def containsDuplicate(self, nums: List[int])-> bool:
        res = set()
        for i in range(len(nums)):
            if nums[i] in res:
                return True
            else:
                res.add(nums[i])
        return False
            


        