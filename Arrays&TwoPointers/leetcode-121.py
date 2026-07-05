'''Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.'''

from typing import List
def maxProfit(prices: List[int]) -> int:
    min_price=prices[0]
    profit=0
    
    for i in prices:
        cur_profit=i-min_price
        if cur_profit>profit:
            profit=cur_profit
        min_price=min(i,min_price)
        