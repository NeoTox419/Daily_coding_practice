#Problem Name: Buy Stock with Transaction Fee
'''
INTUITION:
This is a classic stock trading problem with a transaction fee.
We want to maximize profit by deciding when to buy and sell.

Key idea:
At any day, we have 2 choices:
1. Hold a stock
2. Not hold a stock

We track two states:
- hold: Maximum profit when we currently hold a stock
- cash: Maximum profit when we do NOT hold a stock

Every time we sell, we pay the transaction fee.

APPROACH:
Initialize:
- hold = -arr[0] (buy stock on first day)
- cash = 0 (no stock, no profit)

Iterate through prices:
For each price:
    - Update cash: either keep previous cash OR sell stock today
        cash = max(cash, hold + price - k)
    
    - Update hold: either keep holding OR buy today
        hold = max(hold, cash - price)

Return cash (since final profit should be without holding stock)

Time Complexity: O(n)
Space Complexity: O(1)
'''
class Solution:
    def maxProfit(self, arr, k):
        
        if not arr:
            return 0
        
        hold = -arr[0]
        cash = 0
        
        for price in arr[1:]:
            prev_cash = cash
            cash = max(cash, hold + price - k)
            hold = max(hold, prev_cash - price)
        
        return cash