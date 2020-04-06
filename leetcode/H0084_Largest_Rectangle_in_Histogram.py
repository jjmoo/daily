from typing import List
from utils import Benchmark

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights: return 0
        min_i, min_h, n = 0, heights[0], len(heights)
        for i, height in enumerate(heights):
            if height < min_h:
                min_i, min_h = i, height
        return max(min_h * n, \
            self.largestRectangleArea(heights[: min_i]), \
            self.largestRectangleArea(heights[min_i + 1 :]))

    def largestRectangleAreaStack(self, heights: List[int]) -> int:
        if not heights: return 0
        def check(i, h):
            nonlocal max_area
            index = i
            while h <= stack[-1][1]:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
            return index
        stack, max_area = [(-1, -1)], 0
        for i, h in enumerate(heights): stack.append((check(i, h), h))
        check(i + 1, 0)
        return max_area


def test(func, name):
    with Benchmark(name):
        print(10, func([2,1,5,6,2,3]))
        print(10000, func([x for x in range(200)]))
        print(3, func([2,1,2]))

test(Solution().largestRectangleAreaStack, 'stack')


# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

# The largest rectangle is shown in the shaded area, which has area = 10 unit.

# Example:

# Input: [2,1,5,6,2,3]
# Output: 10

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/largest-rectangle-in-histogram
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
