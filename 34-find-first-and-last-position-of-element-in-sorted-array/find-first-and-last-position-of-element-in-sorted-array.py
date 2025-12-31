class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(x):
            low = 0
            high = len(nums)
            while low < high:
                mid = low + (high-low)//2
                if nums[mid]<x:
                    low = mid + 1
                else:
                    high = mid
            return low
        def upper_bound(x):
            low = 0
            high = len(nums)
            while low < high:
                mid = low + (high-low)//2
                if nums[mid]<=x:
                    low = mid + 1
                else:
                    high = mid
            return low
        start = lower_bound(target)
        end = upper_bound(target) -1
        if start == len(nums) or nums[start] != target:
            return [-1,-1]
        return [start, end]

        