class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = [(capital[i], profits[i]) for i in range(n)]
        projects.sort(key = lambda x:x[0])

        maxheap = []

        idx = 0

        current_capital = w

        for _ in range(k):
            while idx < n and projects[idx][0] <= current_capital:
                required_capital, profit = projects[idx]
                heapq.heappush(maxheap, -profit)
                idx += 1
            
            if not maxheap:
                break
            
            best_profit = -1 * heapq.heappop(maxheap)

            current_capital += best_profit

        return current_capital