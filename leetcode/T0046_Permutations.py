from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]
        def rec(p, l):
            if len(l) <= 1: return [p + l]
            res = []
            for num in l:
                l1 = list(l); l1.remove(num)
                res.extend(rec(p + [num], l1))
            return res
        return rec([], nums)
    
    def permuteBetter(self, nums: List[int]) -> List[List[int]]:
        if not nums: return [[]]
        n, result = len(nums), []
        def trace(first = 0):
            if first == n - 1: result.append(list(nums))
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                trace(first + 1)
                nums[first], nums[i] = nums[i], nums[first]
        trace(); return result


test = Solution().permuteBetter
print(test([1,2,3,4]))
print(test([]))


# Given a collection of distinct integers, return all possible permutations.

# Example:

# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/permutations
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
