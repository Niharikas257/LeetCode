class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # table = {}
        # for i in nums:
        #     if i not in table:
        #         table[i] = 0
        #     else:
        #         return True
        # return False
        tracker = {}
        
        for item in nums:
            if item not in tracker:
                tracker[item] = 0
            else:
                return True
        
        return False
            
       
            
            
        