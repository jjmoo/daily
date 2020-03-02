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
