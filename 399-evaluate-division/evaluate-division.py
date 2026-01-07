# class Solution:
#     def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
#         graph = defaultdict(list)
#         n = len(equations)
#         for i in range(n):
#             graph[equations[i][0]].append((equations[i][1], values[i]))
#             graph[equations[i][1]].append((equations[i][0], 1.0/values[i]))
#         def bfs(src: str, dst: str) -> float:
#             # Undefined variables
#             if src not in graph or dst not in graph:
#                 return -1.0

#             # Same variable
#             if src == dst:
#                 return 1.0

#             q = deque([(src, 1.0)])
#             visited = set([src])

#             while q:
#                 node, ratio = q.popleft()

#                 if node == dst:
#                     return ratio

#                 for nei, w in graph[node]:
#                     if nei in visited:
#                         continue
#                     visited.add(nei)
#                     q.append((nei, ratio * w))

#             return -1.0

#         return [bfs(c, d) for c, d in queries]

from typing import List, Dict

class WeightedDSU:
    def __init__(self) -> None:
        self.parent: Dict[str, str] = {}
        self.weight: Dict[str, float] = {}  # weight[x] = x / parent[x]
        self.rank: Dict[str, int] = {}

    def add(self, x: str) -> None:
        if x not in self.parent:
            self.parent[x] = x
            self.weight[x] = 1.0
            self.rank[x] = 0

    def find(self, x: str) -> str:
        if self.parent[x] != x:
            orig_parent = self.parent[x]
            root = self.find(orig_parent)
            self.weight[x] *= self.weight[orig_parent]  
            self.parent[x] = root
        return self.parent[x]

    def union(self, a: str, b: str, value: float) -> None:
        self.add(a)
        self.add(b)

        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return

        if self.rank[root_a] < self.rank[root_b]:
            self.parent[root_a] = root_b
            self.weight[root_a] = value * self.weight[b] / self.weight[a]
        elif self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a
            self.weight[root_b] = self.weight[a] / (value * self.weight[b])
        else:
            self.parent[root_a] = root_b
            self.weight[root_a] = value * self.weight[b] / self.weight[a]
            self.rank[root_b] += 1


class Solution:
    def calcEquation(
        self,
        equations: List[List[str]],
        values: List[float],
        queries: List[List[str]]
    ) -> List[float]:

        dsu = WeightedDSU()

        for (a, b), val in zip(equations, values):
            dsu.union(a, b, val)

        ans: List[float] = []
        for c, d in queries:
            if c not in dsu.parent or d not in dsu.parent:
                ans.append(-1.0)
                continue

            root_c = dsu.find(c)
            root_d = dsu.find(d)

            if root_c != root_d:
                ans.append(-1.0)
                continue

            # weight[c] = c / root, weight[d] = d / root
            ans.append(dsu.weight[c] / dsu.weight[d])

        return ans


        