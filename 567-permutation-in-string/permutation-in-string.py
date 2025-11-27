class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        need = [0] * 26
        window = [0] * 26
        
        for ch in s1:
            need[ord(ch) - ord('a')] += 1
        
        l = 0
        for r in range(len(s2)):
            window[ord(s2[r]) - ord('a')] += 1
            
            # shrink to keep window size == len(s1)
            if r - l + 1 > len(s1):
                window[ord(s2[l]) - ord('a')] -= 1
                l += 1
            
            # compare frequency arrays
            if window == need:
                return True
        
        return False
