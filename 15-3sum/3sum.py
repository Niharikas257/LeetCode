class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            if num > 0: # if the number you are talking about is positive, there are no chances that you will get a number smaller than that to make the sum zero.
                break
            if i >0 and num == nums[i-1]:
                continue
            left = i+1
            right= len(nums) - 1
            while left < right:
                three_sum = num + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else: 
                    res.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left -1] and left<right:
                        left+=1
        
        return res

