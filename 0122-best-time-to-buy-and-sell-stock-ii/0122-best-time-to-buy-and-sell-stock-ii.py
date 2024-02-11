class Solution(object):
    def maxProfit(self, prices):
        prof=0
        for i in range (1,len(prices)):
            if prices[i] >prices[i-1]:
                prof+=prices[i]-prices[i-1]
        return prof
        