class Solution:
    def jump(self, nums: List[int]) -> int:
        # 1. you start from zero index, and max you can go is nums[0] + 0
        # 2. from 2nd index, max you can go is 1 + nums[1]
        # 3. you jump when max(cur_sum+nums[], num[])
        # we jump when we are the max_so_far

        jump = 0
        max_so_far = 0
        cur_range = 0

        for i in range(len(nums)-1):
            reach = i + nums[i]
            if reach > max_so_far:
                max_so_far = reach
            
            if i == cur_range:
                jump += 1
                cur_range = max_so_far
            if cur_range > len(nums) - 1:
                return jump
        return jump
