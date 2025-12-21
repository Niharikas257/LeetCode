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

        seen = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in seen:
                return [i, seen[remainder]]
            seen[nums[i]] = i
        return []
