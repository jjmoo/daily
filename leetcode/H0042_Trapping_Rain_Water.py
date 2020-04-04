from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        left, right, result = 0, len(height) - 1, 0
        max_left, max_right = height[left], height[right]
        while left < right:
            if max_left <= max_right:
                result += max_left - height[left]
                left += 1
                max_left = max(max_left, height[left])
            else:
                result += max_right - height[right]
                right -= 1
                max_right = max(max_right, height[right])
        return result


test = Solution().trap
print(6, test([0,1,0,2,1,0,1,3,2,1,2,1]))


# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

# Example:

# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/trapping-rain-water
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
