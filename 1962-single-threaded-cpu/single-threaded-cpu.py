class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        indexed = [(tasks[i][0], tasks[i][1], i) for i in range(len(tasks))]
        indexed.sort(key = lambda x:x[0])
        n = len(tasks)
        minheap = []
        time = 0
        i = 0
        result = []

        while len(result) < n:
            if not minheap and time < indexed[i][0]:
                time = indexed[i][0]
            # time += 1
            while i < n and indexed[i][0] <= time:
                enqueue_time, processing_time, index = indexed[i]
                heapq.heappush(minheap, (processing_time,index))
                i += 1
            
            processing_t, ind = heapq.heappop(minheap)
            result.append(ind)
            time += processing_t
        return result
        
# First you enqueue the task into the CPU, that means the current time is more than the enqueue time, because if current time is lesser than the enqueue time, how would the CPU know that there are incoming requests.
# so, if the current_time >= enqueue time, and there are more than we need to help CPU decide based on the processing time, so basically we are pushing the tasks into the minheap only when the enqueue time is less than the current time and then minheap will tell the CPU to decide which one to take. 
# Now, when the already present elements are in the minheap, we pop the element with smallest processing time and if not then the index.
# After we pop the element, we will increase the time to time + processing time because during that time the CPU did not do any other task, now that the current time has increased, if the CPU has not seen any more tasks, then it will process the one already on the heap, otherwise, we will anyways push the new task which CPU encountered while processing, so the CPU now will process the one with less processing time irrespective of which element came first. 
# Now, if the CPU is ideal for a long time, we will make the current_time reach the time of the next available element.
# Also, realize that, CPU idle when minheap is empty.