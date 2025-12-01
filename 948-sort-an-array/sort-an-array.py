class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        minheap = [num for num in nums]
        heapq.heapify(minheap)
        res = []
        while minheap:
            res.append(heapq.heappop(minheap))
        return res
        # minheap = []
        # res = []
        # for num in nums:
        #     heapq.heappush(minheap, num)
        #     heapq.heapify(minheap)
        #     res.append(heapq.heappop(minheap))
        # return res

        