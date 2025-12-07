class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_so_far = 0
        for i in range(len(nums)):
            if i > max_so_far:
                return False
                
            reach = i + nums[i]
            if reach > max_so_far:
                max_so_far = reach
            
            if max_so_far > len(nums)-1:
                return True
        return True
