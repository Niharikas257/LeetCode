class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 1. If it's already sorted, we can use convering 2 pointers, binary search, greedy selection, 
        # 2. no duplicates
        # 3. There are 2 ways of solving - one is you traverse the array and as soon as the value becomes more than target, you return that index
        # 3 another way is to use binary search

        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) //2
            if target > nums[mid]:
                low = mid+1
            elif target < nums[mid]:
                high = mid - 1
            else:
                return mid
        return low