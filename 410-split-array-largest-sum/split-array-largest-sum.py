class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def isValid(target, k):
            cur_sum = 0
            x = k
            for num in nums:
                if cur_sum + num > target:
                    k -= 1
                    cur_sum = num
                    if k == 0:
                        return False
                else:
                    cur_sum += num
            return True

        low = max(nums)
        high = sum(nums)
        while low < high :
            mid = low + (high - low) // 2
            if isValid(mid, k):
                high = mid
            else:
                low = mid + 1
        return low

