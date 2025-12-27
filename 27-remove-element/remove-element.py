class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 1. we can sort the array, we can count the number of elements equal to val and subtract it from the total number of elements.
        # 2. we can use read and write pointers, keep reading from the read pointer and place the write at the place where the next valid pointer should be present.
        # 3. we can use a hashmap also, in which we can store the frequency and simplt return the difference between the total elements and freq of the invalid number

        read = 0
        write = 0
        for read in range(len(nums)):
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1
        return write


        