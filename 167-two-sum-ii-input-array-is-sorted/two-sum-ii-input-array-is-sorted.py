class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(numbers)):
            comp = target - numbers[i]
            if comp in seen:
                return (seen[comp]+1, i+1)
            seen[numbers[i]] = i

            
        
        