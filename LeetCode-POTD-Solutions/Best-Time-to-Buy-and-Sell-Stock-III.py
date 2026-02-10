1class Solution(object):
2    def maxProfit(self, prices):
3        if not prices:
4            return 0
5
6        # 4 states:
7        # buy1  = max profit after 1st buy
8        # sell1 = max profit after 1st sell
9        # buy2  = max profit after 2nd buy
10        # sell2 = max profit after 2nd sell
11
12        buy1 = -prices[0]
13        sell1 = 0
14        buy2 = -prices[0]
15        sell2 = 0
16
17        for price in prices:
18            # Update states in correct order
19            buy1 = max(buy1, -price)             # first buy
20            sell1 = max(sell1, buy1 + price)     # first sell
21            buy2 = max(buy2, sell1 - price)      # second buy
22            sell2 = max(sell2, buy2 + price)     # second sell
23
24        return sell2
25