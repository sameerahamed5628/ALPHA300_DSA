class Solution(object):
    def maxProfit(self, prices):
        low=prices[0]
        profit=0
        for rate in prices:
            if rate<low:
                low=rate
            elif rate-low>profit:
                profit=rate-low
        return profit