class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # l = 0
        # r = len(nums) - 1

        # while l <= r:
        #     m = (l+r)//2
            
        #     if target == nums[m]:
        #         return m

        #     if nums[l]<=nums[m]:

        #         if target < nums[l] or target > nums[m]:
        #             l = m+1
        #         else:
        #             r = m -1

        #     else:

        #         if target > nums[r] or target < nums[m]:
        #             r = m-1
        #         else:
        #             l = m+1
        # return -1

        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low +(high-low)//2
            if target == nums[mid]:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid-1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else: 
                    high = mid - 1
        return -1
            

        
