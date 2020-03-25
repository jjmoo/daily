from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        if 1 == k: return list(nums)
        result, queue, max_num = [], deque(), - 2 ** 31
        for i in range(k - 2, -1, -1):
            max_num = max(max_num, nums[i])
            if not queue or nums[i] > queue[0][0]:
                queue.appendleft((max_num, 1))
            else:
                max_num, cnt = queue.popleft()
                queue.appendleft((max_num, cnt + 1))
        for i in range(k - 1, len(nums)):
            cnt = 1
            while queue and nums[i] >= queue[-1][0]:
                cnt += queue.pop()[1]
            queue.append((nums[i], cnt))
            value, cnt = queue.popleft()
            result.append(value)
            if cnt > 1:
                queue.appendleft((value, cnt - 1))
        return result

    def maxSlidingWindowIndex(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        if 1 == k: return list(nums)
        result, queue, max_num = [], deque(), - 2 ** 31
        for i in range(k - 2, -1, -1):
            if nums[i] > max_num:
                max_num = nums[i]
                queue.appendleft(i)
        for i in range(k - 1, len(nums)):
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
            result.append(nums[queue[0]])
            if queue[0] == i - k + 1: queue.popleft()
        return result

    def maxSlidingWindowSplit(self, nums: List[int], k: int) -> List[int]:
        result, n = [], len(nums)
        left, right = [0] * n, [0] * n
        left[0], right[-1] = nums[0], nums[-1]
        for i in range(1, n):
            if i % k == 0: left[i] = nums[i]
            else: left[i] = max(left[i - 1], nums[i])
            j = n - 1 - i
            if (j + 1) % k == 0: right[j] = nums[j]
            else: right[j] = max(right[j + 1], nums[j])
        for i in range(n - k + 1):
            result.append(max(right[i], left[i + k - 1]))
        return result


test = Solution().maxSlidingWindowSplit
print([3,3,5,5,6,7], test([1,3,-1,-3,5,3,6,7], 3))


# Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

# Follow up:
# Could you solve it in linear time?

# Example:

# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7] 
# Explanation: 

# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#  

# Constraints:

# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length


# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sliding-window-maximum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
