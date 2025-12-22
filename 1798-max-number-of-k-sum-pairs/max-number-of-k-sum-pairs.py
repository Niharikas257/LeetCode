class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # 1 - When changing the input is allowed.
        # nums.sort()
        # left = 0
        # right = len(nums)-1
        # operations = 0

        # while left < right:
        #     if nums[left] + nums[right] < k:
        #         left += 1
        #     elif nums[left] + nums[right] > k:
        #         right -= 1
        #     else:
        #         operations += 1
        #         left += 1
        #         right -= 1
        # return operations

        # 2 - if we can use extra space, we can use hash.
        seen = {}
        operations = 0
        for i, num in enumerate(nums):
            remainder = k - num
            if seen.get(remainder, 0) > 0:
                operations += 1
                seen[remainder] -= 1
            else:
                seen[num] = seen.get(num,0) + 1
                
        return operations





        