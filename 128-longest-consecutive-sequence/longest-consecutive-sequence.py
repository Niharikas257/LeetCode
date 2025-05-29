class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        pot_seq = 0

        for n in num_set:
            if n-1 not in num_set:
                length = 1
                current = n

                while current+1 in num_set:
                    current += 1
                    length += 1

                pot_seq = max(pot_seq, length)

        return pot_seq




        
        