class Solution:
    def makeGood(self, s: str) -> str:
        result = []

        for c in s:
            if result and result[-1].lower()==c.lower() and result[-1] != c:
                result.pop()
            else:
                result.append(c)
        return ''.join(result)

