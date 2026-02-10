1class Solution(object):
2    def maxProfit(self, prices, fee):
3        hold = -prices[0]   # Max profit when holding a stock
4        cash = 0            # Max profit when not holding a stock
5
6        for price in prices[1:]:
7            prev_hold = hold
8            prev_cash = cash
9
10            # If we hold today: keep holding OR buy today (pay price)
11            hold = max(prev_hold, prev_cash - price)
12
13            # If we are in cash today: keep cash OR sell today (gain price - fee)
14            cash = max(prev_cash, prev_hold + price - fee)
15
16        return cash
17