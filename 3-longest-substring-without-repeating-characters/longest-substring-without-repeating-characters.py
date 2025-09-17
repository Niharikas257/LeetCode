class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # charset = set()
        # left = 0
        # res = 0

        # for right in range(len(s)):
        #     while s[right] in charset:
        #         charset.remove(s[left])
        #         left += 1
        #     charset.add(s[right])
        #     res = max(res, right-left+1)
        # return res

        seen = set()
        n = len(s)
        l = 0
        res = 0
        for i in range(n):
            while s[i] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[i])
            res = max(res, i-l+1)
        return res



 
