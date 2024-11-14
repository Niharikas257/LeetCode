class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        n = len(digits)
        # if digits[n-1]<= 8:
        #     digits[i] += 1
        #     return "".join(result)
        
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
            
        return [1] + digits
          
        