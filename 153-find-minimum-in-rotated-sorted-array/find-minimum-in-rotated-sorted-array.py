class Solution:
    def findMin(self, nums: List[int]) -> int:
        # left = 0
        # right = len(nums)-1

        # while left < right:
        #     mid = (left+right) // 2

        #     if nums[mid] > nums[right]:
        #         left = mid + 1
        #     else:
        #         right = mid 
        # return nums[left]

        low = 0
        high = len(nums) - 1

        while low < high:
            mid = low + (high-low) // 2
            if nums[mid] <= nums[high]:
                high = mid
            else:
                low = mid + 1
        return nums[low]
        


            

