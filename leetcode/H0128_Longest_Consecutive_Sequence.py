from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        class Interval:
            def __init__(self, num):
                self.start = num
                self.end = num
            def joinLeft(self, other):
                self.start = other.start
                return self
            def joinRight(self, other):
                self.end = other.end
                return self
        def check(i):
            if i.start - 1 in data:
                left = data[i.start - 1]
                if left.end == i.start - 1:
                    if left.end != left.start: data.pop(left.end)
                    data[i.end] = left.joinRight(i)
                    if i.start != i.end: data.pop(i.start)
                    check(left)
            elif i.end + 1 in data:
                right = data[i.end + 1]
                if right.start == i.end + 1:
                    if right.start != right.end: data.pop(right.start)
                    data[i.start] = right.joinLeft(i)
                    if i.end != i.start: data.pop(i.end)
                    check(right)
        data, result = {}, 1
        for num in nums:
            if num in data: continue
            check(data.setdefault(num, Interval(num)))  
        for k in data:
            result = max(result, data[k].end - data[k].start + 1)
        return result

    def longestConsecutiveSet(self, nums: List[int]) -> int:
        if not nums: return 0
        data, result = set(nums), 0
        for num in data:
            if num - 1 not in data:
                cur, l = num, 1
                while cur + 1 in data:
                    cur, l = cur + 1, l + 1
                result = max(result, l)
        return result


test = Solution().longestConsecutive
print(4, test([100,4,200,1,3,2]))


# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

# Your algorithm should run in O(n) complexity.

# Example:

# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-consecutive-sequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
