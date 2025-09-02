class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        left =[0]*n
        right = [0] *n

        left_set = set()
        for i in range(n):
            left_set.add(s[i])
            left[i] = len(left_set)
        
        right_set = set()
        for i in range(n-1, -1, -1):
            right_set.add(s[i])
            right[i] = len(right_set)

        count = 0
        for i in range(n-1):
            if left[i] == right[i+1]:
                count += 1
        
        return count


