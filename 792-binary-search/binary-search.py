class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1

        # left = 0
        # right = len(nums) - 1

        # while left <= right:
        #     mid = (left+right)//2
        #     if target<nums[mid]:
        #         right = mid - 1
        #     elif target > nums[mid]:
        #         left = mid+1
        #     else:
        #         return mid
        # return -1

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid -1
            else:
                return mid
        return -1









