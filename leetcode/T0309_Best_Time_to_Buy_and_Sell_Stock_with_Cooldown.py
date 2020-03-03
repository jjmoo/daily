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


# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
# Example:

# Input: [1,2,3,0,2]
# Output: 3 
# Explanation: transactions = [buy, sell, cooldown, buy, sell]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
