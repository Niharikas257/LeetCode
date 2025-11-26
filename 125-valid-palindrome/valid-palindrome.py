class Solution:
    def isPalindrome(self, s: str) -> bool:
        # newstr = ""
        # for c in s:
        #     if c.isalnum():
        #         newstr += c.lower()
            
        # return newstr == newstr[::-1]


#  1. create a new empty string
#  2. start iterating over the characters and if it is alphanumeric, add it to the new empty string and convert it to lower.
#  3. return True if the new string which is only alphanumeric and lower case matches exactly with the reversed new string.

#  1. we can have 2 pointers left and right
#  2. run the loop while left < right
#  3. while comparing we need to convert it to the lower case and also, we need to skip the character if it is not alphanumeric

        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1 
            while right > left and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
            

