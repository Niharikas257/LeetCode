# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         res = []
#         digitToChar = {
#             "2": "abc",
#             "3": "def",
#             "4": "ghi",
#             "5": "jkl",
#             "6": "mno",
#             "7": "qprs",
#             "8": "tuv",
#             "9": "wxyz",
#         }
#         def dfs(i, subset): 
#             # i will track the digits
#             if len(subset) == len(digits):
#                 res.append(subset)
#                 return
#             for c in digitToChar[digits[i]]:
#                 dfs(i+1, subset + c)
#         if digits:
#             dfs(0,"")
#         return res
        
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        def backtrack(i, path):
            if i == len(digits):
                res.append("".join(path))
                return

            possibleLetters = digitToChar[digits[i]]
            for letter in possibleLetters:
                path.append(letter)
                backtrack(i+1, path)
                path.pop()
        backtrack(0,[])
        return res

