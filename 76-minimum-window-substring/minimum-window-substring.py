class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c,0)

        left = 0
        window = {}
        res= [-1,-1]
        resLen = float("infinity")
        what_we_have = 0
        what_we_need = len(countT)

        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c,0)

            if c in countT and window[c] == countT[c]:
                what_we_have += 1

            while what_we_have == what_we_need:
                if (right-left+1)< resLen:
                    res = [left,right]
                    resLen = (right-left+1)

                window[s[left]] -= 1
                if s[left] in t and window[s[left]] < countT[s[left]]:
                    what_we_have -= 1
                left += 1
        left,right = res
        return s[left:right+1] if resLen!=float("infinity") else ""


        





            

            
   



        
        