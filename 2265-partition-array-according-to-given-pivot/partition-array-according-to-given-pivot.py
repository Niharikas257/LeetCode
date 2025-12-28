class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # low = 0
        # high = len(nums) - 1
        # mid = 0
        # while mid <= high:
        #     if nums[mid] < pivot:
        #         nums[low], nums[mid] = nums[mid], nums[low]
        #         low += 1
        #         mid += 1
        #     elif nums[mid] > pivot:
        #         nums[mid], nums[high] = nums[high], nums[mid]
        #         high -=1 
        #     else:
        #         mid +=1 
        # return nums

        low = []
        mid = []
        high = []
        for num in nums:
            if num < pivot:
                low.append(num)
            elif num > pivot:
                high.append(num)
            else:
                mid.append(num)
        return low + mid + high