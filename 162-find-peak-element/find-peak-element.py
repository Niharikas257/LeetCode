class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        maxheap = []
        for i, num in enumerate(nums):
            heapq.heappush(maxheap, (-num, i))
        _, i = heapq.heappop(maxheap)
        return i
        
        # left = 0
        # right = len(nums)-1

        # while left < right:
        #     mid = (left+right)//2
        #     if nums[mid] < nums[mid+1]:
        #         left = mid + 1
        #     else:
        #         right = mid
        # return right


        # a = max(nums)
        # for i,num in enumerate(nums):
        #     if num == a:
        #         return i

