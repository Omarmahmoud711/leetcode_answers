class Solution(object):
    def maxProfit(self, prices):
        buy=0
        sell=1
        max_prof=0
        while sell<len(prices):
            if prices[sell] < prices[buy] :
                buy=sell
                sell+=1
            else :
                if max_prof < (prices[sell]-prices[buy]):
                    max_prof=prices[sell]-prices[buy]
                sell+=1
        return max_prof



