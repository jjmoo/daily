# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

class StockSpanner(object):

    buf_size = 1000
    buf_prices = [0] * buf_size
    buf_counts = [0] * buf_size

    def __init__(self):
        self.tail = 0
        self.buf_prices[0] = 1<<20
        self.buf_counts[0] = 1
        pass

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        self.tail += 1
        if self.tail == self.buf_size:
            self.buf_size += 1000
            self.buf_prices.extend([0] * 1000)
            self.buf_prices.extend([0] * 1000)
        self.buf_prices[self.tail] = price
        self.buf_counts[self.tail] = 1
        while self.buf_prices[self.tail] >= self.buf_prices[self.tail - 1]:
            self.tail -= 1
            self.buf_prices[self.tail] = self.buf_prices[self.tail + 1]
            self.buf_counts[self.tail] += self.buf_counts[self.tail + 1]
        return self.buf_counts[self.tail]


class StockSpannerSimple(object):

    def __init__(self):
        self.stack = [(1<<20, 0)]

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        cnt = 1
        while self.stack[-1][0] <= price:
            cnt += self.stack.pop()[1]
        self.stack.append((price, cnt))
        return self.stack[-1][1]


s = StockSpannerSimple()
print(1, s.next(100))
print(1, s.next(80))
print(1, s.next(60))
print(2, s.next(70))
print(1, s.next(60))
print(4, s.next(75))
print(6, s.next(85))


# Write a class StockSpanner which collects daily price quotes for some stock, and returns the span of that stock's price for the current day.

# The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backwards) for which the price of the stock was less than or equal to today's price.

# For example, if the price of a stock over the next 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6].

#  

# Example 1:

# Input: ["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
# Output: [null,1,1,1,2,1,4,6]
# Explanation: 
# First, S = StockSpanner() is initialized.  Then:
# S.next(100) is called and returns 1,
# S.next(80) is called and returns 1,
# S.next(60) is called and returns 1,
# S.next(70) is called and returns 2,
# S.next(60) is called and returns 1,
# S.next(75) is called and returns 4,
# S.next(85) is called and returns 6.

# Note that (for example) S.next(75) returned 4, because the last 4 prices
# (including today's price of 75) were less than or equal to today's price.
#  

# Note:

# Calls to StockSpanner.next(int price) will have 1 <= price <= 10^5.
# There will be at most 10000 calls to StockSpanner.next per test case.
# There will be at most 150000 calls to StockSpanner.next across all test cases.
# The total time limit for this problem has been reduced by 75% for C++, and 50% for all other languages.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/online-stock-span
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
