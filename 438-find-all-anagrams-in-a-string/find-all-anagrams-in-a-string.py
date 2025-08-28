class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if len(p) > len(s):
            return res
        
        countP = Counter(p)
        window = Counter()

        for right in range(len(s)):
            window[s[right]] += 1

            if right >= len(p):
                left = s[right-len(p)]
                window[left] -= 1
                if window[left] == 0:
                    del window[left]

            if window == countP:
                res.append(right-len(p)+1)
        return res
                


 
