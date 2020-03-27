import heapq as hp

class MedianFinder:
    def __init__(self):
        self.lo, self.hi = [2 ** 31 - 1], [2 ** 31 - 1]

    def addNum(self, num: int) -> None:
        if num < self.hi[0]: hp.heappush(self.lo, -num)
        else: hp.heappush(self.hi, num)
        while len(self.hi) > len(self.lo):
            hp.heappush(self.lo, -hp.heappop(self.hi))
        while len(self.lo) > len(self.hi) + 1:
            hp.heappush(self.hi, -hp.heappop(self.lo))

    def findMedian(self) -> float:
        if len(self.lo) == len(self.hi):
            return (self.hi[0] - self.lo[0]) / 2
        else: return - self.lo[0]


finder = MedianFinder()
finder.addNum(1)
finder.addNum(2)
print(1.5, finder.findMedian())
finder.addNum(3)
print(2, finder.findMedian())


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

# For example,
# [2,3,4], the median is 3

# [2,3], the median is (2 + 3) / 2 = 2.5

# Design a data structure that supports the following two operations:

# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.

# Example:

# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2

# Follow up:

# If all integer numbers from the stream are between 0 and 100, how would you optimize it?
# If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-median-from-data-stream
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
