class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(dict)
        for (A,B) , value in zip (equations, values):
            graph[A][B] = value
            graph[B][A] = 1/value
        
        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0
            
            queue = deque([(start, 1.0)])
            visited = set([start])
            
            while queue:
                current, product = queue.popleft()
                if current == end:
                    return product
                
                for neighbor, value in graph[current].items():
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, product*value))
                        
            return -1.0
        
        result = []
        for C,D in queries:
            result.append(bfs(C,D))
            
        return result
                    