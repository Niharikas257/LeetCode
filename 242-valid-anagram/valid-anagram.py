class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table = {}
        if len(s) != len(t):
            return False
        
        for i in s:
            if i in table:
                table[i] += 1
            else:
                table[i] = 1
            
        for j in t:
            if j not in table or table[j] == 0:
                return False
            table[j] -= 1
        
        return True

        # table = {}
        # if len(s) != len(t):
        #     return False

        # for i in s:
        #     if i in table:
        #         table[i] += 1
        #     else:
        #         table[i] = 1

        # for j in t:
        #         if j not in table or table[j] == 0 :
        #             return False
        #         table[j] -= 1
        # return True


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         table = {}
#         for ch in s:
#             table[ch] = table.get(ch, 0) + 1
#         for ch in t:
#             if ch not in table or table[ch] == 0:
#                 return False
#             table[ch] -= 1

#         return True



        