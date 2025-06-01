class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # l = 0
        # r = 1
        # max_profit = 0

        # while r < len(prices):
        #     if prices[l]<prices[r]:
        #         profit = prices[r]-prices[l]
        #         max_profit = max(max_profit, profit)
        #     else:
        #         l = r
        #     r += 1
        # return max_profit


        
        max_profit = 0
        min_buy = prices[0]

        for sell in prices:
            max_profit = max(max_profit, sell-min_buy)
            min_buy = min(min_buy, sell)

        return max_profit
               