class Solution:
    def hIndex(self, citations: List[int]) -> int:

        low = 0
        # h = 0
        n = len(citations)
        high = n
        while low < high :
            mid = low + (high-low)//2
            paper_with_atleast_mid_citations = n - mid
            if citations[mid] >= paper_with_atleast_mid_citations :
                high = mid
            else :
                low = mid + 1
        return 0 if low == n else (n-low)
        