class Solution:
    def findMin(self, nums: List[int]) -> int:
        # for i in range(0, len(nums)-1):
        #     # j = i +1
        #     if nums[i+1]< nums[i]:
        #         return nums[i+1]
        #         # print('Hello')
        
        # return nums[0]
        l = 0
        r = len(nums)-1
        res = 0
        while l < r:
            m = (l+r)//2
            if nums[m]< nums[r]:
                r =m
                
            else:
                l = m + 1
        return nums[l]

            

