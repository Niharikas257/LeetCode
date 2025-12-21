class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # numSet = set(nums)
        # longest = 0
        # for num in numSet:
        #     if (num - 1) not in numSet:
        #         length = 1
        #         while (num + length) in numSet:
        #             length += 1
        #         longest = max(length, longest)
        # return longest
################
        store = set(nums)
        res = 0
        for num in store:
            if (num - 1) not in store:
                streak = 1 # If the smaller number does not exist in the store, that means it could be the start of a streak.
                while (num + streak) in store:
                    streak += 1
                res = max(res, streak)
        return res

        # res = 0
        # store = set(nums)
        # for num in nums:
        #     streak = 0
        #     cur_element = num
        #     while cur_element in store:
        #         streak += 1
        #         cur_element += 1
        #     res = max(res, streak)
        # return res\

        seen = set(nums)
        streak_len = 0
        longest = 0
        for num in nums:
            if (num - 1) not in seen:
                start_of_streak = num
                streak_len += 1
            if start_of_streak + 1 in seen:
                start_of_streak += 1
                streak_len += 1
            longest = max(longest, streak_len)
        return longest








        
        