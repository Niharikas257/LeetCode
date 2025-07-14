from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def palindrome(sub):
            stack = []
            mid = len(sub)//2      # use sub, not s
            n = len(sub)           # use sub, not s
            for i in range(mid):
                stack.append(sub[i])
            start = mid if n % 2 == 0 else mid + 1
            for i in range(start, n):
                if not stack or sub[i] != stack.pop():
                    return False
            return True
        
        res = []
        def dfs(i, subset):
            if i == len(s): 
                res.append(subset.copy())
                return
            for j in range(i, len(s)):
                sub = s[i:j+1]
                if palindrome(sub):
                    subset.append(sub)
                    dfs(j+1, subset)
                    subset.pop()
        dfs(0, [])
        return res
