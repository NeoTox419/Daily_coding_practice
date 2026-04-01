'''
Intuition:
----------
To maximize profit with only one transaction (one buy and one sell),
we want to buy the stock at the lowest possible price and sell it later
at the highest possible price after that buy day.

While scanning the prices day by day:
- Keep track of the minimum price seen so far (best day to buy).
- For each day, calculate the profit if we sell on that day.
- Update the maximum profit found so far.

If prices keep decreasing, no profit is possible, so return 0.
'''

'''
Approach:
---------
1. Initialize:
    - min_price = infinity (to track lowest price so far)
    - max_profit = 0
2. Traverse the prices array:
    - Update min_price if current price is lower.
    - Calculate profit = current price - min_price.
    - Update max_profit if profit is higher.
3. Return max_profit.
'''

class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0

        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit
