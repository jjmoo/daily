class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        k, profit = 0, [[0, float('-inf'), 0] for _ in range(2)]
        for price in prices:
            profit[1 - k][0] = max(profit[k][0], profit[k][2])
            profit[1 - k][1] = max(profit[k][1], profit[k][0] - price)
            profit[1 - k][2] = profit[k][1] + price
            k ^= 1
        return max(profit[k])

    def maxProfitBetter(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        sold, keep, last_sold = 0, float('-inf'), 0
        for price in prices:
            last = sold
            sold = max(sold, keep + price)
            keep = max(keep, last_sold - price)
            last_sold = last
        return sold


print(1, Solution().maxProfitBetter([1,2]))
print(3, Solution().maxProfitBetter([1,2,3,0,2]))
print(4, Solution().maxProfitBetter([1,2,3,0,0,2]))
print(6, Solution().maxProfitBetter([6,1,3,2,4,7]))
print(15, Solution().maxProfitBetter([2,6,8,7,8,7,9,4,1,2,4,5,8]))
