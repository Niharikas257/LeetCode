class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_val = 0
        jump_reach = 0

        for i in range(len(nums)):
            if i > max_val:
                return False

            jump_reach = i + nums[i]

            if jump_reach > max_val:
                max_val = jump_reach
    
            if max_val > len(nums)-1 :
                return True

        return True

            

        