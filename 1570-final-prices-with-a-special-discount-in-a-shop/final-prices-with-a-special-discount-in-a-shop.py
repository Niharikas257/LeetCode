class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = [] # price, index
        answer = [0]*len(prices)
        for i,price in enumerate(prices):
            while stack and stack[-1][0] >= price:
                popped_price, popped_index = stack.pop()
                answer[popped_index] = popped_price - price

            stack.append((price, i))

        while stack:
            price, index = stack.pop()
            answer[index] = price
        return answer
