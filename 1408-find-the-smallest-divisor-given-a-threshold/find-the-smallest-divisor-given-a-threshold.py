class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def isValid(denominator):
            # res = []
            cur_sum = 0
            for num in nums:
                # res.append(ceil(num//denominator))
                cur_sum += ceil(num/denominator)
                if cur_sum > threshold:
                    return False
            return True

        low = 1
        high = max(nums)
        while low <= high :
            mid = low +(high - low) // 2
            if isValid(mid):
                high = mid -1
            else:
                low = mid + 1
        return low
            
        