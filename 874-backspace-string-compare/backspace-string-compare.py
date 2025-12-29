class Solution:
    def valid_char(self, s, index):
        skip = 0
        while index >= 0:
            if s[index] == '#':
                skip += 1
                index -= 1
            elif skip > 0:
                skip -= 1
                index -= 1
            else:
                break
        return index
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1
        while i >= 0 or j >= 0:
            i = self.valid_char(s, i)
            j = self.valid_char(t,j)
            if i< 0 and j < 0:
                return True
            elif i >= 0 and j>=0:
                if s[i] != t[j]:
                    return False
            else:
                return False
            i -= 1
            j -= 1
        return True

        # def build(text):
        #     stack = []
        #     for ch in text:
        #         if ch == "#":
        #             if stack :
        #                 stack.pop()
        #         else:
        #             stack.append(ch)
        #     return stack

        # return build(s) == build(t)

        




        