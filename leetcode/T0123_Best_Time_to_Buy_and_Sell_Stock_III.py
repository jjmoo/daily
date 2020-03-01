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
