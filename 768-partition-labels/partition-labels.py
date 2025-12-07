class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_pos = {}
        for i, ch in enumerate(s):
            last_pos[ch] = i # end of the character
        start = 0
        end = 0 # end of the segment
        res = []
        
        for i, ch in enumerate(s):
            end = max(end, last_pos[ch])

            if i == end:
                res.append(end-start+1)
                start = i+1
        return res



        