class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count = Counter(tasks) # this line will count the number of each tasks and push it into a hash table which will have the numer of elements and the frequency of each. so, technically this hash will have keys and values
        # maxheap = [-i for i in count.values()] # this line will create a maxheap array with just the values from the count hash table, because we need only the values(frequencies) to push into the heap.
        # heapq.heapify(maxheap) # we are converting this maxheap array into the actual heap now.
        # time = 0
        # q = deque() # we will need a queue to push the values for cool down period and pull it back from the queue to the heap when the cool down period is over.
        # while maxheap or q :
        #     time += 1
        #     if not maxheap:
        #         time = q[0][1]
        #     else: 
        #         cnt = heapq.heappop(maxheap) + 1 # we add 1 because in maxheap we add negative values.
        #         if cnt:
        #             q.append([cnt, (time+n)])
        #     if q and q[0][1] == time:
        #         heapq.heappush(maxheap, q.popleft()[0])
        # return time
        count = Counter(tasks)
        maxheap = [-i for i in count.values()]
        heapq.heapify(maxheap)
        time = 0
        q = deque()

        while maxheap or q:
            time += 1
            if not maxheap:
                time = q[0][1]
            else:
                cnt = heapq.heappop(maxheap) + 1
                if cnt:
                    q.append([cnt, (time+n)])
            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])

        return time



        