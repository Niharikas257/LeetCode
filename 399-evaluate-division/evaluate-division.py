class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        n = len(equations)
        for i in range(n):
            graph[equations[i][0]].append((equations[i][1], values[i]))
            graph[equations[i][1]].append((equations[i][0], 1.0/values[i]))
        def bfs(src: str, dst: str) -> float:
            # Undefined variables
            if src not in graph or dst not in graph:
                return -1.0

            # Same variable
            if src == dst:
                return 1.0

            q = deque([(src, 1.0)])
            visited = set([src])

            while q:
                node, ratio = q.popleft()

                if node == dst:
                    return ratio

                for nei, w in graph[node]:
                    if nei in visited:
                        continue
                    visited.add(nei)
                    q.append((nei, ratio * w))

            return -1.0

        return [bfs(c, d) for c, d in queries]


        