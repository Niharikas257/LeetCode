class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        # Step 1: Find the global dominant element using Boyer-Moore Majority Vote algorithm.
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        dom = candidate  # The dominant element
        
        # Count how many times the dominant element appears in the whole array.
        global_count = nums.count(dom)
        
        left_count = 0
        # Step 2: Check for valid split indices.
        for i in range(n - 1):
            if nums[i] == dom:
                left_count += 1
            # Check if the left subarray has a dominant element.
            if left_count * 2 <= (i + 1):
                continue
            # For the right subarray.
            right_count = global_count - left_count
            if right_count * 2 > (n - i - 1):
                return i
        return -1
