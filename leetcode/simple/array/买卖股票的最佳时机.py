class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total=0
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                total+=prices[i+1]-prices[i]
        print total
s=Solution()
s.maxProfit([7,6,4,3,1])