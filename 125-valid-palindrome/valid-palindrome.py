class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for c in s:
            if c.isalnum():
                new += c.lower()
        return new == new[::-1]
    #     left = 0
    #     right = len(s) -1
    #     while left < right:
    #         while left < right and not self.alphaNum(s[left]):
    #             left += 1
    #         while right > left and not self.alphaNum(s[right]):
    #             right -= 1
    #         if s[left].lower() != s[right].lower():
    #             return False
    #         left += 1
    #         right -= 1

    #     return True
    
    # def alphaNum(self, c):
    #     return (ord('a')<= ord(c) <= ord('z') or
    #             ord('A') <= ord(c) <= ord('Z') or 
    #             ord('0') <= ord(c) <= ord('9'))


