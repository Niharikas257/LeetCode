class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)

        if m > n:
            return False

        count1 = [0]*26
        count2 = [0]*26

        for i in range(m):
            # range m because we need to find maximum of length m (length of s1)
            count1[ord(s1[i])- ord('a')] += 1
            count2[ord(s2[i])- ord('a')] += 1
        
        if count1 == count2:
            return True

        for r in range(m,n):
            count2[ord(s2[r])-ord('a')] += 1
            count2[ord(s2[r-m])-ord('a')] -= 1

            if count1 == count2:
                return True
        
        return False


        