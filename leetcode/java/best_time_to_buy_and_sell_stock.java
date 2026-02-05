class Solution {
    public int maxProfit(int[] prices) {
        int max_profit = 0;

        int min_price_to_buy = prices[0];
        for( int i = 1; i < prices.length; i++ )
        {
            // If current price is less, buy the stock for current price
            if(prices[i] < min_price_to_buy)
            {
                min_price_to_buy = prices[i];
            }
            // If profit is max with current price, sell the stock for current price and update max_profit
            else if (prices[i] > min_price_to_buy)
            {
                if ((prices[i] - min_price_to_buy) > max_profit)
                {
                    max_profit = prices[i] - min_price_to_buy;
                }   
            }
        }
        return max_profit;
    }
}
