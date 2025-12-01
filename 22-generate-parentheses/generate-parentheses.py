class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []

        def backtrack(open, close):
            if open == n and close == n:
                res.append("".join(path))
                return res
            
            if open < n:
                path.append("(")
                backtrack(open+1, close)
                path.pop()
            
            if close < open:
                path.append(")")
                backtrack(open, close+1)
                path.pop()
            
        backtrack(0,0)
        return res
