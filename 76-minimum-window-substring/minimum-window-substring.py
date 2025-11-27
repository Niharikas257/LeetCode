class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        Hash_T = {}

        for ch in t:
            Hash_T[ch] = Hash_T.get(ch,0) + 1
        
        need = len(Hash_T)
        have = 0
        res = [-1,-1]

        left = 0
        window = {}
        min_val = float("infinity")
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            if s[right] in Hash_T and window[s[right]] == Hash_T[s[right]]:
                have += 1

            while need == have:
                if (right - left + 1) < min_val:
                    res = [left, right]
                    min_val = (right - left + 1)


                window[s[left]] -= 1
                if s[left] in Hash_T and Hash_T[s[left]] > window[s[left]]:
                    have -= 1

                left += 1
            
        left, right = res
        return s[left : right + 1] if min_val != float("infinity") else ""





        

        


        





            

            
   



        
        