from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return 0
        dp0, dp1, max_product = 1, 1, - 2 ** 31
        for num in nums:
            t0, t1 = dp0 * num, dp1 * num
            dp0, dp1 = min(num, t0, t1), max(num, t0, t1)
            if dp1 > max_product:
                max_product = dp1
        return max_product


test = Solution().maxProduct
print(6, test([2,3,-2,4]))
print(0, test([-2,0,-1]))
print(12, test([-3,-4]))
print(24, test([-2,3,-4]))
print(-2, test([-2]))


# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

# Example 1:

# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-product-subarray
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
