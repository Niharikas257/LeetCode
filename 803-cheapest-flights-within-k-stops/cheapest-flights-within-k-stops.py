class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = [float("inf")]* n
        cost[src] = 0

        for _ in range(k+1):
            temp = cost.copy()
            for u, v, price in flights:
                if cost[u] == float("inf"):
                    continue
                new_cost = price + cost[u]
                if new_cost < temp[v]:
                    temp[v] = new_cost
            cost = temp
        return -1 if cost[dst] == float("inf") else cost[dst]
