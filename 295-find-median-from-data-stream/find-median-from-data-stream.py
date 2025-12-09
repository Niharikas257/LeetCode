class MedianFinder:

    def __init__(self):
        self.small = [] #maxheap
        self.large = [] # minheap
        
    def addNum(self, num: int) -> None:

        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1* num)
        
        if len(self.large) > len(self.small) +1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

        if len(self.small) > len(self.large) +1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (self.large[0] + -1 * (self.small[0])) / 2.0      


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# class MedianFinder:

#     def __init__(self):
#         self.large = [] # -> minheap, the root is the smallest element after the median
#         self.small = [] #-> maxheap, the root is the largest element before the median

#     def addNum(self, num: int) -> None:
#         if self.large and num > self.large[0]:
#             heapq.heappush(self.large, num)
#         # if self.small and num < self.small[0]:
#         else:
#             heapq.heappush(self.small, -1 * num)
#         if len(self.small) > len(self.large) + 1:
#             val = -1 * heapq.heappop(self.small)
#             heapq.heappush(self.large, val)
#         if len(self.large) > len(self.small) + 1:
#             val = heapq.heappop(self.large)
#             heapq.heappush(self.small, -1 * val) 

#     def findMedian(self) -> float:
#         if len(self.small) > len(self.large):
#             return -1*self.small[0]
#         elif len(self.large) > len(self.small):
#             return self.large[0]
        
#         return (-1*self.small[0] + self.large[0])/2.0
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()