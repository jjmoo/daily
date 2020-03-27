class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 0 or not arr:
            return 0
        sum_left, min_left, max_left, sum_mid, max_mid = 0, 0, 0, 0, 0
        for num in arr:
            sum_left += num
            sum_mid += num
            if sum_left < min_left:
                min_left = sum_left
                sum_mid = 0
            if sum_left > max_left:
                max_left = sum_left
            if sum_mid > max_mid:
                max_mid = sum_mid
        max_right = sum_left - min_left
        max_single = max(max_left, max_right, max_mid)
        if k is 1:
            return max_single
        else:
            max_mid = max(0, sum_left * (k - 2))
            return max(max_single, max_left + max_right + max_mid) % (10**9 + 7)


print(9, Solution().kConcatenationMaxSum([1,2], 3))
print(2, Solution().kConcatenationMaxSum([1,-2,1], 5))
print(0, Solution().kConcatenationMaxSum([-1,-2], 7))
print(8, Solution().kConcatenationMaxSum([3,-9,3,0,5,-4], 1))
print(1, Solution().kConcatenationMaxSum([-2,1,-2], 10))


# Given an integer array arr and an integer k, modify the array by repeating it k times.

# For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].

# Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be 0 and its sum in that case is 0.

# As the answer can be very large, return the answer modulo 10^9 + 7.

#  

# Example 1:

# Input: arr = [1,2], k = 3
# Output: 9
# Example 2:

# Input: arr = [1,-2,1], k = 5
# Output: 2
# Example 3:

# Input: arr = [-1,-2], k = 7
# Output: 0
#  

# Constraints:

# 1 <= arr.length <= 10^5
# 1 <= k <= 10^5
# -10^4 <= arr[i] <= 10^4

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/k-concatenation-maximum-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
