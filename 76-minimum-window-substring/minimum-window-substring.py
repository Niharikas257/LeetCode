class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        targetcount = {}
        window = {}

        for c in t:
            targetcount[c] = 1 + targetcount.get(c, 0)
        
        need = len(targetcount)
        have = 0
        l = 0
        res = [-1,-1]
        resLen=float("infinity")
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)

            if c in targetcount and targetcount[c] == window[c]:
                have += 1
            
            while have == need:
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r-l+1
                window[s[l]] -= 1
                if s[l] in targetcount and window[s[l]]<targetcount[s[l]]:
                    have -= 1
                l+=1

        l,r = res
        return s[l : r + 1] if resLen != float("infinity") else ""
        # return s[l : r + 1] if resLen != float("infinity") else ""




            

            
   



        
        