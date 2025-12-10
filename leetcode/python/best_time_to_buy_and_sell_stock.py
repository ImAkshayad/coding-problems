class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price_to_buy = prices[0]
        for i in range(1,len(prices)):
            # If current price is less, buy the stock for current price
            if prices[i] < min_price_to_buy:
                min_price_to_buy = prices[i]
                # If profit is max with current price, sell the stock for current price 
            elif prices[i] > min_price_to_buy:
                if (prices[i] - min_price_to_buy) > max_profit:
                    max_profit = prices[i] - min_price_to_buy
        return max_profit