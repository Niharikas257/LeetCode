class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            freq[task] = 1 + freq.get(task,0)
        
        maxheap = []
        for task, count in freq.items():
            heapq.heappush(maxheap, (-count, task))
        
        q = deque()
        time = 0

        while maxheap or q:
            time += 1
            while q and q[0][0] <= time:
                ready_time, ready_count, ready_task= q.popleft()
                heapq.heappush(maxheap, (ready_count, ready_task))            
            if maxheap:
                count, task = heapq.heappop(maxheap)
                count += 1
                if count < 0:
                    q.append((time + n + 1, count, task))
        return time
                




                


