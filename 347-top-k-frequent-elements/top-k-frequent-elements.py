class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        heap = []
        for i in count.keys():
            heapq.heappush(heap, (count[i], i))
            if len(heap)>k:
                heapq.heappop(heap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        # count = {}
        # for num in nums:
        #     count[num] = 1+count.get(num,0)

        # heap = []
        # for num in count.keys():
        #     heapq.heappush(heap,(count[num], num))
        #     if len(heap)>k:
        #         heapq.heappop(heap)

        # res = []
        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])
        # return res

    #    1. Create a hash map
    #    2. start entering the frequencies
    #    3. we can use a max-heap, and we pop everytime the size of the heap increases k
    #    4. Now, we need to save the popped values somewhere, so we will create a res array and append the popped values into it.

        