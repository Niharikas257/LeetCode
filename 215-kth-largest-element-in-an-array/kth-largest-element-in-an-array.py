class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxheap = []
        for i in nums:
            heapq.heappush(maxheap, -i)
        res =[]
        while k>0:
            res.append(-heapq.heappop(maxheap))
            k-=1
        
        return res[-1]
        