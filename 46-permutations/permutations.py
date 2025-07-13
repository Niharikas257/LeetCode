class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        
        res = []
        for i in range(len(nums)):
            cur = nums[i]
            remain = nums[:i] + nums[i+1:]
            for p in self.permute(remain):
                res.append([cur] + p)
        return res


        