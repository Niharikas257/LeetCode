class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Hash Set - Set doesn't allow repeated numbers
        # seen = set()
        # for i in nums:
        #     if i in seen:
        #         return i
        #     seen.add(i)
        # return -1
        
        
        # nums_set = set()
        # for num in nums:
        #     if num in nums_set:
        #         return num
        #     nums_set.add(num)
        # return -1

        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow


        
