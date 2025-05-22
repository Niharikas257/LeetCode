from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i, n = 0, len(nums)
        while i < n:
            start = nums[i]
            # consume the consecutive run
            while i + 1 < n and nums[i+1] == nums[i] + 1:
                i += 1
            end = nums[i]
            # emit
            res.append(f"{start}->{end}" if start != end else str(start))
            i += 1
        return res
