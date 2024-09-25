class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []
        
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1 # If the last element is the same as the next element, then we increase the count of the character.
                if stack[-1][1] == k:
                    stack.pop()
                    
            else:
                stack.append([char,1])
        
        result = []
        
        for char, count in stack:
            result.append(char*count)
            
        return ''.join(result)
            
        # return ''.join([(char*count) for char, count in stack])