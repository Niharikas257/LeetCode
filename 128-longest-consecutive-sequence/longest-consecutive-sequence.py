class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numset = set(nums)

        for num in numset:
            if num-1 not in numset:
                length = 1
                current = num
                while (current+1) in numset:
                    current += 1
                    length += 1
                res = max(res, length)
        return res
            





        
        