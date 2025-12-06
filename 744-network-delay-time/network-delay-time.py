class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time_to_reach = {i: float("inf") for i in range(1, n + 1)}
        time_to_reach[k] = 0

        edges = collections.defaultdict(list)
        for (u,v,w) in times:
            edges[u].append((v,w))

        q = [(0, k)] # [(time, node)]
        visited = set()

        while q:
            cur_time, cur_node = heapq.heappop(q)

            if cur_node in visited:
                continue

            visited.add(cur_node)

            for (neighbor, time) in edges[cur_node]:
                new_time = time + cur_time
                if new_time < time_to_reach[neighbor]:
                    time_to_reach[neighbor] = new_time
                    heapq.heappush(q, (new_time, neighbor))
            
        if len(visited) < n:
            return -1
        return max(time_to_reach.values())
