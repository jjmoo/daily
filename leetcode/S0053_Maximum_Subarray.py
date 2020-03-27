from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return -2 ** 31
        sum_left, result = 0, -2 ** 31
        for num in nums:
            sum_left += num
            result = max(result, sum_left)
            if sum_left < 0: sum_left = 0
        return result

    def maxSubArrayDp(self, nums: List[int]) -> int:
        if not nums: return -2 ** 31
        for i in range(1, len(nums)):
            nums[i] += max(0, nums[i - 1])
        return max(nums)


test = Solution().maxSubArrayDp
print(6, test([-2,1,-3,4,-1,2,1,-5,4]))
print(-1, test([-1]))


# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-subarray
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
