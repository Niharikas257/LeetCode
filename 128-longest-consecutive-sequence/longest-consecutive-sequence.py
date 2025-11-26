class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
        # res = 0
        # store = set(nums)
        # for num in nums:
        #     streak = 0
        #     cur_element = num
        #     while cur_element in store:
        #         streak += 1
        #         cur_element += 1
        #     res = max(res, streak)
        # return res
        # store = set(nums)
        # res = 0
        # for num in nums:
        #     streak = 0
        #     if (num-1) not in store:
        #         streak = 1 # If the smaller number does not exist in the store, that means it could be the start of a strak.
        #         while (num+streak) in store:
        #             streak += 1
        #         res = max(res, streak)
        # return res





        
        