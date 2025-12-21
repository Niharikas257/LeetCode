class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # 1. can I change the input - no - no sorting - if we are sorting we need to use hash map with enumerate to store the actual index of the values in the original array.
        #                           - yes - sorting
        # 2. can I use extra space - no - no hashing
        #                          - yes - hash or set
        # 3. is the data contiguous - no - we just need indices, we don't need the range - no prefix/ sliding window.


        # left = 0
        # right = len(nums)-1

        # while left < right:
        #     if nums[left] == nums[right]:
        
        if len(nums) <= 1:
            return False
        nums_idx = [[num, i] for i, num in enumerate(nums)]
        nums_idx.sort()
        for j in range(len(nums_idx)):
            if nums_idx[j][0] == nums_idx[j-1][0] and abs(nums_idx[j][1] - nums_idx[j-1][1]) <= k:
                return True
        return False




        