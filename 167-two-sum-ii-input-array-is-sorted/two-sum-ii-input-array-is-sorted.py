class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, val in enumerate(numbers):
            remainder = target - val
            if remainder in seen:
                return[seen[remainder]+1, i+1]
            seen[val] = i

        