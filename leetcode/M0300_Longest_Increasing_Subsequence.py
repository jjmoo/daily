from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        n, l_max = len(nums), 1
        memo = [1] * n
        for j in range(1, n):
            l_max_j = 0
            for i in range(j):
                l = 1 + (memo[i] if nums[j] > nums[i] else 0)
                if l > l_max_j: l_max_j = l
            memo[j] = l_max_j
            if l_max_j > l_max: l_max = l_max_j
        return l_max

    def lengthOfLISBetter(self, nums: List[int]) -> int:
        if not nums: return 0
        import bisect
        n, memo = len(nums), [nums[0]]
        for j in range(1, n):
            p = bisect.bisect_left(memo, nums[j])
            if p == len(memo): memo.append(nums[j])
            else: memo[p] = nums[j]
        return len(memo)


test = Solution().lengthOfLISBetter
print(3, test([4,10,4,3,8,9]))
print(4, test([10,9,2,5,3,7,101,18]))
print(1, test([10]))


# Given an unsorted array of integers, find the length of longest increasing subsequence.

# Example:

# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
# Note:

# There may be more than one LIS combination, it is only necessary for you to return the length.
# Your algorithm should run in O(n^2) complexity.
# Follow up: Could you improve it to O(n log n) time complexity?

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
