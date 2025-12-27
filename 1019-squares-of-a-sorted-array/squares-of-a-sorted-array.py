class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            res.append(num*num)
        res.sort()
        return res
        

        left = 0
        right = len(nums)-1
        res = [0]*n
        write = len(nums) - 1
        while left < right:
            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]
            if left_square > right_square:
                res[write] = left_square
                left += 1 
            elif left_square < right_square:
                res[write] = right_square
                right -= 1
            write -= 1
        return res