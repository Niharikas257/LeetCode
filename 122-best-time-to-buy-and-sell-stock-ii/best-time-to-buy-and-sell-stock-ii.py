class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 0
        max_profit = 0
        profit = 0
        cur_profit = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                cur_profit += profit
            
            # elif prices[right] < prices[left]:
            left = right
            
            right += 1
        return cur_profit
        