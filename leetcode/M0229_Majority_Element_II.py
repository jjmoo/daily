from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        can1, can2, cnt1, cnt2 = 0, 0, 0, 0
        for num in nums:
            if cnt1 > 0 and cnt2 > 0:
                if num == can1: cnt1 += 1
                elif num == can2: cnt2 += 1
                else: cnt1, cnt2 = cnt1 - 1, cnt2 - 1
            elif cnt1 == 0:
                if can2 == num: cnt2 += 1
                else: can1, cnt1 = num, 1
            else:
                if can1 == num: cnt1 += 1
                else: can2, cnt2 = num, 1
        counter, n = {}, len(nums)
        if cnt1 > 0: counter[can1] = 0
        if cnt2 > 0: counter[can2] = 0
        for num in nums:
            if num in counter: counter[num] += 1
        return [key for key in counter if n // counter[key] < 3]


test = Solution().majorityElement
print(3, test([3,2,3]))
print(1, 2, test([1,1,1,3,3,2,2,2]))
print(3, test([3,2,3,1]))
print([], test([1,2,3,4]))


# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

# Note: The algorithm should run in linear time and in O(1) space.

# Example 1:

# Input: [3,2,3]
# Output: [3]
# Example 2:

# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/majority-element-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
