class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        profit = 0
        last = prices[0]
        for price in prices:
            profit += max(0, price - last)
            last = price
        return profit


print(Solution().maxProfit([])) # 0
print(Solution().maxProfit(None)) # 0
print(Solution().maxProfit([7,1,5,3,6,4])) # 7
print(Solution().maxProfit([1,2,3,4,5])) # 4
print(Solution().maxProfit([7,6,4,3,1])) # 0
