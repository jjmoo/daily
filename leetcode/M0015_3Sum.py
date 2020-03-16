class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if not nums: return result
        n = len(nums)
        if n <= 2: return result
        nums.sort()
        i = 0
        while i < n - 2:
            j, k = i + 1, n - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] <= 0:
                    if nums[i] + nums[j] + nums[k] == 0:
                        result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j - 1] == nums[j]:
                        j += 1 
                else:
                    k -= 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < n - 2 and nums[i - 1] == nums[i]:
                i += 1
        return result


test = Solution().threeSum
print([[-1,0,1],[-1,-1,2]], test([-1,0,1,2,-1,-4]))
print([], test([]))


# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
