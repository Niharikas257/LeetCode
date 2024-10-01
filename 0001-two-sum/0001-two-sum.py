class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map={}
        
        for index,value in enumerate(nums):
            remainder=target-value
            
            if remainder in hash_map:
                return [hash_map[remainder], index]
            
            hash_map[value]=index
            
        