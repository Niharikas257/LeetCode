class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        for num in nums:
            heapq.heappush(minheap, num)
            if len(minheap) > k:
                heapq.heappop(minheap) # When you pop from the heap if the len becomes more than k means there are just k elements in the heap, and because this is a minheap, so the popped value is the smallest value which we anyways don't need. So, heap has k values which and does not have values which we don't need. In other words, heap has k larger values because we are popping the smaller values. So, at any point when you add a value, the smaller one goes to the top and if the size of the heap exceeds k that means heap has more than k values so we need to pop, and we pop the value which we don't need which is the smaller value. So, heap top has smallest of larger values.
        return minheap[0]

