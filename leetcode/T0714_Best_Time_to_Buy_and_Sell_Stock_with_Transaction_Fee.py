class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices:
            return 0
        sold, keep = 0, -1<<31
        for price in prices:
            last_sold = sold
            sold = max(sold, keep + price - fee)
            keep = max(keep, last_sold - price)
        return sold


print(8, Solution().maxProfit([1, 3, 2, 8, 4, 9], fee = 2))
