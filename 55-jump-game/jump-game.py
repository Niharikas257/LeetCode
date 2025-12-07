class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0
        max_so_far = nums[0]
        for i in range(len(nums)):
            # 1. if I am at a position in the array where I can't reach while jumping, then return False
            # 2. Also, how will I know if I can not reach here ?
            # 3. I need to track the maximum reach from all the positions, and if that position matches where I am then I can reach here.
            # 4. How will I the maximum reach?
            # 5. The maximum reach from a position is i + nums[i], because I am already at i and can jump nums[i]
            # 6. I will call i + nums[i] = reachable because if i + nums[i] is an index (less than the len(nums)) where I can reach, then it means it is reachable by me.
            if i > reachable:
                return False
            reachable = max(reachable, i + nums[i])

            # 7. If I am at i which is not reachable, then I need to update the value of reachable
            if max_so_far > reachable:
                reachable = max_so_far

            if reachable >= len(nums) - 1:
                return True
        return True
  