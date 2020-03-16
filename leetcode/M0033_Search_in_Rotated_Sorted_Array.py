from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        import bisect
        def bi_search(i, j):
            p = bisect.bisect_left(nums, target, i, j + 1)
            return p if p != j + 1 and nums[p] == target else -1
        def rotate_search(i, j):
            if i == j or i + 1 == j:
                return i if nums[i] == target else (j if nums[j] == target else -1)
            m = (i + j) // 2
            if nums[i] <= nums[m]:
                return max(bi_search(i, m), rotate_search(m + 1, j))
            else:
                return max(rotate_search(i, m), bi_search(m + 1, j))
        return rotate_search(0, len(nums) - 1)


test = Solution().search
print(4, test([4,5,6,7,0,1,2], 0))
print(-1, test([4,5,6,7,8,0,1,2], 3))
print(-1, test([], 5))

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Your algorithm's runtime complexity must be in the order of O(log n).

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
