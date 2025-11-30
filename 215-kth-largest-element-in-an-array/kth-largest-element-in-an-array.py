class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k +1
        minheap = [num for num in nums]
        heapq.heapify(minheap)
        res = []

        while len(res)<k:
            res.append(heapq.heappop(minheap))
            # print(res)
        return res[-1]


# import heapq
# from typing import List

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         minheap = []

#         for num in nums:
#             heapq.heappush(minheap, num)
#             if len(minheap) > k:
#                 heapq.heappop(minheap)    # kick out smallest, keep only k largest

#         return minheap[0]                 # root = kth largest
