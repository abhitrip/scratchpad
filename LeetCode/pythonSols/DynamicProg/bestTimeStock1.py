class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """ Normal Algorithm
        if len(prices)<1:
            return 0

        leastUptoNow = prices[0]
        maxprofit = 0
        for price in prices:
            maxprofit = max(price-leastUptoNow,maxprofit)
            leastUptoNow = min(leastUptoNow,price)

        return maxprofit
        """
        # Kadane's algorithm which is dp - max contiguous sum
        maxProfitNow,maxSoFar = 0,0
        for i in range(1,len(prices)):
            maxProfitNow = max(0,maxProfitNow + prices[i]-prices[i-1])
            maxSoFar = max(maxSoFar,maxProfitNow)

        return maxSoFar







