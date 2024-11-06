class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """
        for target in (tops[0], bottoms[0]):
            missingT = 0
            missingB = 0
            
            for i, (top, bottom) in enumerate(zip(tops, bottoms)):
                if not(top == target or bottom == target):
                    break
                if top!= target:
                    missingT += 1
                if bottom != target:
                    missingB += 1
                    
                if i == len(tops)-1:
                    return min(missingT, missingB)
            
        return -1