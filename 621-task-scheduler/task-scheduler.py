class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        q = deque()
        freqs = Counter(tasks)
        maxheap = [-freq for freq in freqs.values()]
        heapq.heapify(maxheap)
        time = 0

        while maxheap or q:
            time += 1
            if maxheap:
                freq = 1 + heapq.heappop(maxheap)
                if freq:
                    q.append([freq, time + n])
                
            if q and q[0][1] == time:
                heapq.heappush(maxheap, q.popleft()[0])
        print(time)
        return time
                


