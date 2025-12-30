class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
# one pass to erase all the extra closed brackets, another pass for extra open brackets
        # open = 0
        # res = []
        # erase = 0
        # for i in range(len(s)):
        #     if s[i] == "(":
        #         open += 1
        #         res.append(s[i])
        #     elif s[i] == ")":
        #         if open > 0:
        #             open -= 1
        #             res.append(s[i])
        #         else:
        #             erase += 1
        #     else:
        #         res.append(s[i])
        # result = []
        # for i in range(len(res)-1, -1, -1):
        #     if res[i] == "(" and open > 0:
        #         open -=1
        #     else:
        #         result.append(res[i])
        # result.reverse()
        # return "".join(result)

        stack = []
        s = list(s)
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack:
                    stack.pop()
                    # s[i] = ''
                else:
                    s[i] = ''
        while stack:
            s[stack.pop()] = ''
        return "".join(s)



        




                

        