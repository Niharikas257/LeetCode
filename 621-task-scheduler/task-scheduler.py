class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1. A...wait for 2T then A then wait for 2T...
        # 2. meanwhile, we can have other tasks or if there are no other tasks, we can leave it blank
        # 3. A _ _ A _ _ A 
        #    1 2 3 4 5 6 7
           
        #    time = 0

        #    time += 1
        # 4. we need to spread the elements with maximum frequency first and then fill up the space, 2nd frequent element

            freqs = Counter(tasks)
            q = deque() # [frequency, time]
            time = 0
            maxheap = [-freq for freq in freqs.values()]
            heapq.heapify(maxheap)

            while maxheap or q:
                time += 1
                if maxheap:
                    freq = 1 + heapq.heappop(maxheap)
                    if freq:
                        q.append([freq, time+n])

                    
                if q and q[0][1] == time:
                    heapq.heappush(maxheap, q.popleft()[0])
                
            return time



