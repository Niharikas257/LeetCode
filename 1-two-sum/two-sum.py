class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        store = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            # if rem not in store:
            #     store[nums[i]] = i
            if rem in store:
                return [i, store[rem]]
            store[nums[i]] = i
        return []
        