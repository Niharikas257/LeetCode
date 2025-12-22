class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 1. It should not change the input
        # 2. We can not use hash
        # 3. we do not need contiguous or continuous values - so no prefic or sliding window

        n = len(nums)
        i = 0

        while i < n:
            correct_index = nums[i] - 1

            if 1 <= nums[i] <= n and nums[correct_index] != nums[i]:
                # swap
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1
            
        
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1
            
          




        



        