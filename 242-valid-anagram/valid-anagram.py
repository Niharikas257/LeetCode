class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        S = list(s)
        T = list(t)
        if len(S) != len(T):
            return False
        S.sort()
        T.sort()
        # return S == T
        # count = len(S)
        # cnt = 0
        for i in range(len(S)):
            # for j in range(len(T)):
            if S[i] != T[i]:
                return False

        return True
                
        
                    
