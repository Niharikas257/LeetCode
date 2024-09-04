class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        l, r = 0, len(s)-1
        
        while l<r:
            while l<r and not self.alphanumeric(s[l]):
                l+=1
            while r>l and not self.alphanumeric(s[r]):
                r-=1
            if s[l].lower()!=s[r].lower():
                return False
            l,r=l+1, r-1
            
        return True
    
    def alphanumeric(self, c):
            return (ord('a')<= ord(c)<= ord('z') or ord('0')<= ord(c)<= ord('9') or ord('A')<= ord(c)<= ord('Z'))

                   
                   
    
            
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

                
            
                
            
            # s=s.lower()
        # filtered_s=''.join(char for char in s if char.isalnum())
        # return filtered_s==filtered_s[::-1]
        
#         newstr=""
        
#         for c in s:
#             if c.isalnum():
#                 newstr+=c.lower()
#         return newstr == newstr[::-1]