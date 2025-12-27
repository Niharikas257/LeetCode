class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        max_sum = 0

        left = 0
        right = n-1

        while left < right:
            max_sum = max(max_sum, nums[left] + nums[right])
            left += 1
            right -= 1
        
        return max_sum

        