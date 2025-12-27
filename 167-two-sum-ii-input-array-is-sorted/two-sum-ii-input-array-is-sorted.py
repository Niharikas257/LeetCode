class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # seen = {}
        # for i, val in enumerate(numbers):
        #     remainder = target - val
        #     if remainder in seen:
        #         return[seen[remainder]+1, i+1]
        #     seen[val] = i

# 1. we can create a hashmap and use the remainder, if it's in the hashmap then return the index

# 1. we can use 2 pointer technique, because the array is already sorted, so we can add left + right values and if it's bigger than target, we move left, else, we go right
        # left = 0
        # right = len(numbers) - 1
        # while left<right:
        #     sum = numbers[left] + numbers[right]
        #     if sum == target:
        #         return [left+1, right+1]
        #     elif sum < target:
        #         left += 1
        #     else:
        #         right -= 1

        left =  0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else: 
                return [left+1, right+1]        

        