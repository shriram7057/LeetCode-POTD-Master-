1class Solution(object):
2    def maxProfit(self, prices):
3        if not prices:
4            return 0
5
6        # States:
7        # hold = max profit while holding a stock
8        # sold = max profit when we just sold today
9        # rest = max profit when we are not holding and not selling today (cooldown or doing nothing)
10
11        hold = -prices[0]
12        sold = 0
13        rest = 0
14
15        for price in prices[1:]:
16            prev_hold = hold
17            prev_sold = sold
18            prev_rest = rest
19
20            # If we hold today: either we were already holding, or we buy today from rest state
21            hold = max(prev_hold, prev_rest - price)
22
23            # If we sold today: we must have held yesterday
24            sold = prev_hold + price
25
26            # If we rest today: either we rested yesterday or just sold yesterday
27            rest = max(prev_rest, prev_sold)
28
29        # Maximum profit is in not holding a stock (either rest or sold)
30        return max(sold, rest)
31