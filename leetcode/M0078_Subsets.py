from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [[]] if not nums else [[x for j, x in enumerate(nums) if i & (1 << j)] for i in range(2 ** len(nums))]


test = Solution().subsets
for l in test([1,2,3]): print(l)


# Given a set of distinct integers, nums, return all possible subsets (the power set).

# Note: The solution set must not contain duplicate subsets.

# Example:

# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/subsets
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
