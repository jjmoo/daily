from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        i, n, offset_min = 0, len(nums), 2**31-1
        while i < n - 2:
            j, k = i + 1, n - 1
            while j < k:
                offset = nums[i] + nums[j] + nums[k] - target
                if offset == 0: return target
                if abs(offset) < abs(offset_min):
                    offset_min = offset
                if offset < 0: j += 1
                else: k -= 1
            i += 1
        return target + offset_min


test = Solution().threeSumClosest
print(2, test([-1, 2, 1, -4], 1))
print(3, test([0,1,2], 3))
print(2, test([1,1,1,0], -100))


# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

# Example:

# Given array nums = [-1, 2, 1, -4], and target = 1.

# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum-closest
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
