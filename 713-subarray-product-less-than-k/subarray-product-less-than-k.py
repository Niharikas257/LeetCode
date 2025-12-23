class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # def atmost(k):
        product = 1
        left = 0
        # window = []
        count = 0
        if k <= 1:
            return 0

        for right in range(len(nums)):
            product *= nums[right]
            # window.append(nums[right])
            while product >= k and left <= right:
                product //= nums[left]
                left += 1
        
            count += right - left + 1
        return count






        