class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digits_to_char = {  "2":"abc",
                            "3":"def",
                            "4":"ghi",
                            "5":"jkl",
                            "6":"mno",
                            "7":"pqrs",
                            "8":"tuv",
                            "9":"wxyz" }

        # res = []
        # path = []

        # def dfs(index):
        #     if index == len(digits):
        #         res.append("".join(path.copy()))
        #         return
        #     for ch in digits_to_char[digits[index]]:
        #         path.append(ch)
        #         dfs(index+1)
        #         path.pop()
        # dfs(0)
        # return res
        
        res = []
        path = []

        def dfs(index):
            if index == len(digits):
                res.append("".join(path.copy()))
                return
            for ch in digits_to_char[digits[index]]:
                path.append(ch)
                dfs(index+1)
                path.pop()
        dfs(0)
        return res

 
