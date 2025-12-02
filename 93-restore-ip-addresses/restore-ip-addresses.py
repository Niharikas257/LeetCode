class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(start, part):
            if len(part) == 4:
                if start == len(s):
                    res.append(".".join(part))
                return res
            
            remaining = len(s) - start
            remaining_parts = 4 - len(part)

            # for j in range(len(remaining)):
            if remaining < remaining_parts or remaining > 3 * remaining_parts:
                return 
            for length in range(1, 4): # This for loop is for the segments
                end = start + length
                if end >len(s):
                    break
                if s[start] == '0' and length > 1:
                    continue
                if int(s[start:end]) > 255:
                    continue

                part.append(s[start:end])
                backtrack(end, part)
                part.pop()
        backtrack(0,[])
        return res


        