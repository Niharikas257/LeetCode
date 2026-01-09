class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # 1. You are using maxheap to make choice when the capital is enough for multiple projects, in that case, you will choose the project with maximum profit.
        n = len(profits)
        index = 0
        current_capital = w
        best_profit = 0
        maxheap = []
        projects = [(capital[i], profits[i]) for i in range(n)]
        projects.sort(key=lambda x:x[0]) # we will start from the one which needs minimum capital
        for _ in range(k): # Run the loop k times, we don't require the variable that's why _
            while index < len(projects) and current_capital >= projects[index][0]:
                required_capital, profit = projects[index]
                heapq.heappush(maxheap, -profit) # If we have enough capital to start a project, we will pick the one with maximum profit.
                index +=1 
            
            if not maxheap:
                break
            
            best_profit = -1*heapq.heappop(maxheap)
            current_capital += best_profit
        
        return current_capital

