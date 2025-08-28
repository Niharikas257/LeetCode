class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charset = set(s)

        for c in charset:
            left = 0
            count = 0
            for right in range(len(s)):
                if s[right] == c:
                    count += 1
                while (right-left+1) - count > k:
                    if s[left] == c:
                        count -= 1
                    left += 1
                res = max(res, right-left+1)
        return res

 