class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = nums
        self.k = k
        heapq.heapify(self.minheap)
        # while len(self.minheap) > k:
        #     heapq.heappop(self.minheap)
        # You need to trim the heap size in __init__ because if the size of minheap before first add is bigger than k, let's say m, then add will only pop the element to make it m-1, not k.     
    def add(self, val):
        heapq.heappush(self.minheap, val)
        while len(self.minheap) > self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
    
        

