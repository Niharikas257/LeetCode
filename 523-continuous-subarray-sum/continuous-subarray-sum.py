class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        if k == 0: # Means the sum should be zero
            prefix = 0
            seen = {0:-1}
            for i, num in enumerate(nums):
                prefix += num
                if prefix in seen:
                    prev_index = seen[prefix]
                    if i - prev_index >= 2:
                        return True
                else:
                    seen[preix] = i
            return False
        else:
            mod_base = abs(k)
            prefix = 0
            seen = {0:-1}
            for i, num in enumerate(nums):
                prefix += num
                remainder = prefix % mod_base
                if remainder in seen:
                    prev_index = seen[remainder]
                    if i - prev_index >= 2:
                        return True
                else:
                    seen[remainder] = i
        return False





