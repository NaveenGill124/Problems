class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = float('inf') # large value
        profit = 0

        for price in prices:

            if price < min_price:
                min_price = price
            
            else:
                profit = max(profit, (price - min_price))

        return profit
