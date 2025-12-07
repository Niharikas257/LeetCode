class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # count = 0
        # j = 0
        # for i in range(len(g)-1):
        #     if s[i] >= s[j]:
        #         count += 1
        #     j+= 1
        #     if j > len(s):
        #         break
        # return count

        i = 0
        j = 0
        count = 0
        g.sort()
        s.sort()
        # for j in range(len(s)):
        while j < len(s) and i < len(g):
            if s[j] >= g[i]:
                i += 1
                j += 1

            else:
                j += 1
        return i
