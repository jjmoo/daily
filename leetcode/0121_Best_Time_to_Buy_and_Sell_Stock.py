class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        min_price = prices[0]
        profit = 0
        for price in prices:
            profit = max(profit, price - min_price)
            min_price = min(min_price, price)
        return profit


print(Solution().maxProfit([])) # 0
print(Solution().maxProfit(None)) # 0
print(Solution().maxProfit([7,1,5,3,6,4])) # 5
print(Solution().maxProfit([7,6,4,3,1])) # 0
