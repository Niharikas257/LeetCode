class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        maxheap = []
        for i, num in enumerate(nums):
            heapq.heappush(maxheap, (-num, i))
        _, i = heapq.heappop(maxheap)
        return i
        