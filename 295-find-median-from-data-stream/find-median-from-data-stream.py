import heapq

class MedianFinder:
    def __init__(self):
        self.left = []   # max-heap via negatives
        self.right = []  # min-heap

    def addNum(self, num: int) -> None:
        # Put into one heap
        if self.right and num > self.right[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.left, -num)  

        # Rebalance sizes: left can have at most 1 extra
        if len(self.left) > len(self.right) + 1:
            heapq.heappush(self.right, -heapq.heappop(self.left))
        elif len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return float(-self.left[0])
        return (-self.left[0] + self.right[0]) / 2.0   
