class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if not nums:
            return 0

        left= 0
        write = 1
        for read in range(len(nums)):
            if nums[read] != nums[write-1]:
                nums[write] = nums[read]
                write += 1
        return write
        