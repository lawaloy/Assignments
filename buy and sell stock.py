class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        maxProfit = 0
        minimum = float("inf")
        for price in prices:
            if price < minimum:
                minimum = price
            else:
                maxProfit = max(maxProfit, price - minimum)
        return maxProfit
