from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums: return 1
        n = len(nums)
        for num in nums:
            while num >= 1 and num <= n and nums[num - 1] != num:
                nums[num - 1], num = num, nums[num - 1]
        for i, num in enumerate(nums):
            if num != i + 1: return i + 1
        return n + 1


test = Solution().firstMissingPositive
print(3, test([1,2,0]))
print(2, test([3,4,-1,1]))
print(1, test([7,8,9,11,12]))
print(6, test([5,2,3,1,4]))


# Given an unsorted integer array, find the smallest missing positive integer.

# Example 1:

# Input: [1,2,0]
# Output: 3
# Example 2:

# Input: [3,4,-1,1]
# Output: 2
# Example 3:

# Input: [7,8,9,11,12]
# Output: 1
# Note:

# Your algorithm should run in O(n) time and uses constant extra space.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/first-missing-positive
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
