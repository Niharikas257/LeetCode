class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # left = 0
        # right = 0
        # count = {}
        # max_freq =  0
        # res = 0

        # for right in range(len(s)):
        #     count[s[right]] = count.get(s[right], 0) + 1
        #     max_freq = max(max_freq, count[s[right]])
        #     while (right-left+1)  - max_freq > k:
        #         count[s[left]] -= 1
        #         left +=1
        #     res = max(res, right-left+1)
        # return res

        left = 0
        right = 0
        window = {}
        max_freq = 0
        res = 0

        for right in range(len(s)):
            window[s[right]] = window.get(s[right],0)+1
            max_freq = max(max_freq, window[s[right]])
            while (right-left+1) - max_freq > k:
                window[s[left]] -= 1
                left += 1
            res = max(res, right-left+1)
        return res

                

