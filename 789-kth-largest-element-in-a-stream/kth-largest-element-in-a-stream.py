class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        # Now this nums/ self.minHeap is just an array, we need to heapify it so this array will have the properties of the min heap
        heapq.heapify(self.minHeap)
        while len(self.minHeap)> self.k:
            heapq.heappop(self.minHeap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) # This will push the value in the min heap, maintaining the heap invariant.
        if len(self.minHeap)> self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)