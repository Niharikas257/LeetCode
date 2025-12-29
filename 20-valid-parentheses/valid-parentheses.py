class Solution:
    def isValid(self, s: str) -> bool:
        stack  = []
        opentoclose = { ")" : "(", "]" : "[", "}" : "{" }

        for ch in s:
            if stack and ch in opentoclose:
                if stack[-1] == opentoclose[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return True if not stack else False






