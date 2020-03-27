class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        # record 3 transation
        tr1 = [prices[0], prices[0], 0]
        tr2 = [prices[0], prices[0], 0]
        tr3 = [prices[0], prices[0], 0]
        for price in prices:
            if price <= tr3[0]:
                tr3[0], tr3[1] = price, price
                continue
            if price <= tr3[1]:
                continue
            tr3[1], tr3[2] = price, price - tr3[0]
            # profit for merge 2&3
            mer23 = tr3[1] - tr2[0]
            if mer23 > tr2[2] and mer23 > tr3[2] and mer23 > tr3[2] + tr2[2] - tr1[2]:
                # merge 2&3
                tr2[1], tr2[2] = tr3[1], mer23
                tr3[0], tr3[1] = price, price
            else:
                # lost if merge 1&2
                lost12 = tr1[2] + tr2[2] - tr2[1] + tr1[0]
                if lost12 < tr1[2] and lost12 < tr2[2]:
                    if tr3[2] > lost12:
                        # merge 1&2
                        tr1[1], tr1[2] = tr2[1], tr2[1] - tr1[0]
                        tr2[0], tr2[1], tr2[2] = tr3[0], tr3[1], tr3[2]
                        tr3[0], tr3[1] = price, price
                        pass
                elif tr1[2] <= tr2[2]:
                    if tr3[2] > tr1[2]:
                        # drop 1
                        tr1[0], tr1[1], tr1[2] = tr2[0], tr2[1], tr2[2]
                        tr2[0], tr2[1], tr2[2] = tr3[0], tr3[1], tr3[2]
                        tr3[0], tr3[1] = price, price
                        pass
                else:
                    if tr3[2] > tr2[2]:
                        #drop 2
                        tr2[0], tr2[1], tr2[2] = tr3[0], tr3[1], tr3[2]
                        tr3[0], tr3[1] = price, price
                        pass
        return tr1[2] + tr2[2]

    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        size = len(prices)
        left, right = [0] * size, [0] * size
        min_left, max_right = prices[0], prices[-1]
        for i in range(1, size):
            left[i] = max(left[i - 1], prices[i] - min_left)
            min_left = min(min_left, prices[i])
            right[- i - 1] = max(right[-i], max_right - prices[- i - 1])
            max_right = max(max_right, prices[- i - 1])
        profit = 0
        for i in range(size):
            profit = max(profit, left[i] + right[i])
        return profit


print(Solution().maxProfit([3,3,5,0,0,3,1,4])) # 6
print(Solution().maxProfit([1,2,3,4,5])) # 4
print(Solution().maxProfit([7,6,4,3,1])) # 0
print(Solution().maxProfit([2,1,4])) # 3
print(Solution().maxProfit([6,1,3,2,4,7])) # 7

print(Solution().maxProfit2([3,3,5,0,0,3,1,4])) # 6
print(Solution().maxProfit2([1,2,3,4,5])) # 4
print(Solution().maxProfit2([7,6,4,3,1])) # 0
print(Solution().maxProfit2([2,1,4])) # 3
print(Solution().maxProfit2([6,1,3,2,4,7])) # 7


# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete at most two transactions.

# Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

# Example 1:

# Input: [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
#              Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
# Example 2:

# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
#              Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
#              engaging multiple transactions at the same time. You must sell before buying again.
# Example 3:

# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
