class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return
        current_max = nums[0]
        max_prod = nums[0]
        current_min = nums[0]
        temp_max = nums[0]
        for num in nums[1:]:
            temp_max = max(num, current_max*num, current_min * num)
            current_min = min(num, current_max*num, current_min* num)
            current_max = temp_max
            max_prod = max(max_prod, current_max)
        return max_prod
        
        