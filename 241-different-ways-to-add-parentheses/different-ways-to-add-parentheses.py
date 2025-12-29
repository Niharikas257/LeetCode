class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        results = []
        if len(expression) == 0:
            return results
        
        if len(expression) == 1:
            return [int(expression)]
        
        if len(expression) == 2 and expression[0].isdigit():
            return [int(expression)]

        for i, char in enumerate(expression):
            if char.isdigit():
                continue
            left_results = self.diffWaysToCompute(expression[:i])
            right_results = self.diffWaysToCompute(expression[i+1:])

            for left in left_results:
                for right in right_results:
                    if char == "+":
                        results.append(left+right)
                    elif char == "-":
                        results.append(left-right)
                    if char == "*":
                        results.append(left*right)
        return results
                      