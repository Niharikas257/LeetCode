class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(start, part):
            
            if len(part) == 4:
                if start == len(s):
                    res.append(".".join(part))
                return 

            remaining_part = 4 - len(part)
            remaining = len(s) - start
            
            if remaining < remaining_part or remaining > 3*remaining_part:
                return
            
            for length in range(1,4):
                end = start + length
                if end > len(s):
                    break
                if s[start] == '0' and length > 1:
                    continue
                
                if int(s[start:end])>255:
                    continue
                
                part.append(s[start:end])
                backtrack(end, part)
                part.pop()
        
        backtrack(0, [])
        return res