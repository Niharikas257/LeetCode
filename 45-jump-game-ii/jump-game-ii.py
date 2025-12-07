class Solution:
    def jump(self, nums: List[int]) -> int:
        max_so_far = 0
        count = 0
        current_range = 0

        for i in range(len(nums)-1):

            reach = i + nums[i]
            # print (reach)
            if reach > max_so_far:
                max_so_far = reach

            if i == current_range:
                count += 1
                current_range = max_so_far

            # count += 1
            if current_range >= len(nums)-1:
                return count

        return count
        
        # 1. You are at index zero, you can reach 0 + nums[0]
        # 2. you go to index 1, and can reach 1 + nums[1], pick max( jump from the last value, jump from this value)
        # 3. you jump when