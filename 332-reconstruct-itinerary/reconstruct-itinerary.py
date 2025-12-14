class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # n = len(tickets) - 1
        # graph = [[] for _ in range(n)]
        graph = defaultdict(list)
        for u,v in tickets:
            graph[u].append(v)
        
        for u in graph:
            graph[u].sort(reverse= True)
        
        stack = ["JFK"]
        itinerary = []

        while stack:
            cur_node = stack[-1]

            if graph[cur_node]:
                new_node = graph[cur_node].pop()
                stack.append(new_node)
            else:
                
                itinerary.append(stack.pop())
        itinerary.reverse()
        return itinerary
                



        