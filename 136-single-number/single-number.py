class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # res = 0
        # freq = Counter(nums) # O(1) - creating tha map, but internally it runs n times. so, O(n)

        # # Loop unique element times
        # for (char, count) in freq.items():# gives you all the pairs
        # # loop for "unique number"
        #     if count == 1:
        #         res = char
        # return res
        

        # # O(n) + O(U) =   O(n)

        res =0
        for num in nums:
            res ^= num
        return res