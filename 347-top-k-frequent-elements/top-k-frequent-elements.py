class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. create a hash table for the count of the numbers in the array
        # 2. Use that hash table to create an array with the item and their frequency
        # 3. sort the array based on the frequency
        # 4. create a list res and append the popped values from the array while the length of the res is k.
        # 5. return res
        # count = {}
        # for num in nums:
        #     count[num] = 1 + count.get(num,0)
        
        # arr = []
        # for item, cnt in count.items():
        #     arr.append([cnt, item])
        # arr.sort()

        # res = []
        # while len(res)<k:
        #     res.append(arr.pop()[1])
        # return res


##########        
            #    1. Create a hash map
    #    2. start entering the frequencies
    #    3. we can use a max-heap, and we pop everytime the size of the heap increases k
    #    4. Now, we need to save the popped values somewhere, so we will create a res array and append the popped values into it.

        # count = {}
        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)
        
        # heap = []
        # for i in count.keys():
        #     heapq.heappush(heap, (count[i], i))
        #     if len(heap)>k:
        #         heapq.heappop(heap)
        
        # res = []
        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])
        # return res

        # freq = {}
        # for num in nums:
        #     freq[num] = 1 + freq.get(num, 0)
        
        # minheap = []
        # for i in freq.keys():
        #     heapq.heappush(minheap, (freq[i], i))
        #     if len(minheap) > k:
        #         heapq.heappop(minheap)
        # res = []
        # for i in range(k):
        #     res.append(heapq.heappop(minheap)[1])
        # return res

        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        minheap = [] # we need the most frequent elements means we need the elements with highest frequency.
        for num, frequency_of_num in freq.items():
            heapq.heappush(minheap, (frequency_of_num, num))
            if len(minheap) > k:
                heapq.heappop(minheap)
        res = []
        while minheap:
            res.append(heapq.heappop(minheap)[1])
        return res

        




        