class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums.sort()
        def merge_sort(nums):
            if len(nums) > 1:
                mid = len(nums) // 2  # Find the middle of the array
                left_half = nums[:mid]  # Divide the array into two halves
                right_half = nums[mid:]

                merge_sort(left_half)  # Recursively sort the first half
                merge_sort(right_half)  # Recursively sort the second half

                i = j = k = 0

                # Merge the sorted halves
                while i < len(left_half) and j < len(right_half):
                    if left_half[i] < right_half[j]:
                        nums[k] = left_half[i]
                        i += 1
                    else:
                        nums[k] = right_half[j]
                        j += 1
                    k += 1

                # Copy remaining elements of left_half, if any
                while i < len(left_half):
                    nums[k] = left_half[i]
                    i += 1
                    k += 1

                # Copy remaining elements of right_half, if any
                while j < len(right_half):
                    nums[k] = right_half[j]
                    j += 1
                    k += 1
            return nums

        merge_sort(nums)
