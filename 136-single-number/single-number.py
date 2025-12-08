class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        freq = Counter(nums)
        for (char, count) in freq.items():
            if count == 1:
                res = char
        return res
        