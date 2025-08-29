class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        seen = {0:1}
        count = 0

        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k

            if mod<0:
                mod += k
            
            if mod in seen:
                count += seen[mod]

            seen[mod] = seen.get(mod,0) + 1
        return count