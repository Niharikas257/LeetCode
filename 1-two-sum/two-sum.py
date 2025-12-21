class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 1. can i change the input - yes - sorting
        # 2. can I use extra space - yes - Hash map
        # 3. Is it absolute difference ? - Yes
        # 4. can the values be nagtive - no - sliding window/ prefix

        # seen = {}
        # for i in range(len(nums)):
        #     remainder = target - nums[i]
        #     if remainder in seen:
        #         return [i, seen[remainder]]
        #     seen[nums[i]] = i
        # return []

        nums_idx = [[num, i] for i, num in enumerate(nums)]
        nums_idx.sort()
        left = 0
        right = len(nums_idx)-1
        while left < right:
            if nums_idx[left][0] + nums_idx[right][0] > target:
                right -= 1
            elif nums_idx[left][0] + nums_idx[right][0] < target:
                left += 1
            else:
                return [nums_idx[left][1], nums_idx[right][1]]
