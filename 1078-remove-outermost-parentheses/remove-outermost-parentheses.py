class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        # Basically if you see 2 similar brackets consecutively, you remove one of them.
        stack = []
        res = []
        for ch in s:
            if ch == "(":
                if stack:
                    res.append(ch)
                stack.append(ch)
            else:
                stack.pop()
                if stack:
                    res.append(ch)
        return "".join(res)

