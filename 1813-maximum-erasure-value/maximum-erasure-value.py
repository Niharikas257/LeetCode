class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left, right = 0, 0
        seen = set()
        cur_sum = 0
        best_sum = 0

        for right in range(len(nums)):
            num = nums[right]
            while num in seen:
                seen.remove(nums[left])
                cur_sum -= nums[left]
                left += 1
                
            else:
                seen.add(nums[right])
                cur_sum += nums[right]
            
            # if cur_sum > best_sum:
            #     best_sum = cur_sum
            best_sum = max(best_sum, cur_sum)
        return best_sum

        