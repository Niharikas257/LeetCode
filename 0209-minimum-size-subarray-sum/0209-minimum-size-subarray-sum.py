class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = 0
        min_len = float('inf')
        window_sum = 0
        
        for right in range (n):
            window_sum += nums[right]
            while window_sum >= target:
                #left = left +1
                min_len = min(min_len, right-left+1)
                window_sum = window_sum - nums[left]
                left += 1
        
        if min_len!= float('inf'):
            return min_len
        else:
            return 0
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         n = len(nums)
#         window_sum = 0
#         min_len = float('inf')
#         left = 0
        
        
#         for right in range(n):
#             window_sum += nums[right]
#             # If the sum exceeds the target, then we need to delete the left element while keeping the length minimum.
#             while window_sum >= target:
#                 min_len = min(min_len , right - left + 1)
#                 window_sum -= nums[left]
#                 left += 1
                
#         return min_len if min_len!= float('inf') else 0
            
            