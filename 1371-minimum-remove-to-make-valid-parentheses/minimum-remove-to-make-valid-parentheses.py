class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # def isValid(ch):
        #     if ch == "(":
        #         stack.append(ch)
        #     else:
        #         if not stack:
        #             return False
        #         stack.pop()
        #         return True
                
        #     return False

        # stack  = []
        # res = []
        # for i in range(len(s)):
        #     if s[i].isalnum():
        #         res.append(s[i])
                
        #     elif s[i] == "(":
        #         stack.append(len(res))
        #         res.append(s[i])
        #     elif s[i] == ")":
        #         if isValid(s[i]):
        #             res.append(s[i])
        #     else:
        #         res.append(s[i])
        # return "".join(res)

        open = 0
        res = []
        erase = 0
        for i in range(len(s)):
            if s[i] == "(":
                open += 1
                res.append(s[i])
            elif s[i] == ")":
                if open > 0:
                    open -= 1
                    res.append(s[i])
                else:
                    erase += 1
            else:
                res.append(s[i])
        result = []
        for i in range(len(res)-1, -1, -1):
            if res[i] == "(" and open > 0:
                open -=1
            else:
                result.append(res[i])
        result.reverse()
        return "".join(result)

        




                

        