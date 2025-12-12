class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        window = set()
        res = 0

        # for right in range(len(s)):
        while right <= len(s)-1:
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            
            res = max(res, right - left + 1)
            right += 1
        return res
