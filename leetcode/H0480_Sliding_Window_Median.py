from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if 1 == k: return list(nums)
        import bisect
        result, window, k1, k2 = [], [], (k - 1) >> 1, k >> 1
        for i in range(len(nums)):
            bisect.insort(window, (nums[i], i))
            if i >= k - 1:
                result.append((window[k1][0] + window[k2][0]) / 2)
                window.remove((nums[i - k + 1], i - k + 1))
        return result

    def medianSlidingWindowTwoHeap(self, nums: List[int], k: int) -> List[float]:
        if 1 == k: return list(nums)
        import heapq as hp
        def clean(h):
            while abs(h[0][1]) in de:
                    de.remove(abs(hp.heappop(h)[1]))
        def move(h1, h2):
            clean(h1)
            num, i = hp.heappop(h1)
            hp.heappush(h2, (-num, -i))
        result, bal, odd = [], - ((k + 1) // 2), bool(k & 1)
        lo, hi, de = [], [], set()
        for i, num in enumerate(nums):
            if hi and num < hi[0][0]:
                hp.heappush(lo, (-num, -i))
                bal += 1
            else:
                hp.heappush(hi, (num, i))
            if i >= k - 1:
                while bal < 0:
                    move(hi, lo)
                    bal += 1
                while bal > 0:
                    move(lo, hi)
                    bal -= 1
                clean(lo)
                clean(hi)
                result.append(-lo[0][0] if odd else (hi[0][0] - lo[0][0]) / 2)
                if nums[i - k + 1] <= -lo[0][0]:
                    bal -= 1
                de.add(i - k + 1)
        return result


test = Solution().medianSlidingWindowTwoHeap
print(test([1,3,-1,-3,5,3,6,7], 3))
print(test([1,4,2,3], 4))
print(test([1,1,1,1], 2))
print(test([6,5,9,5,4,9,1,7,5,5], 4))


# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

# Examples:
# [2,3,4] , the median is 3

# [2,3], the median is (2 + 3) / 2 = 2.5

# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

# For example,
# Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

# Window position                Median
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       1
#  1 [3  -1  -3] 5  3  6  7       -1
#  1  3 [-1  -3  5] 3  6  7       -1
#  1  3  -1 [-3  5  3] 6  7       3
#  1  3  -1  -3 [5  3  6] 7       5
#  1  3  -1  -3  5 [3  6  7]      6
# Therefore, return the median sliding window as [1,-1,-1,3,5,6].

# Note: 
# You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array.
# Answers within 10^-5 of the actual value will be accepted as correct.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sliding-window-median
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
