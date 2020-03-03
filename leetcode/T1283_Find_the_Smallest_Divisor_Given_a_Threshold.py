class Solution(object):
    def smallestDivisor(self, nums, threshold):
        """
        :type nums: List[int]
        :type threshold: int
        :rtype: int
        """
        size, sum, num_max = len(nums), 0, 0
        for i in range(size):
            num_max = max(num_max, nums[i])
            nums[i] -= 1
            sum += nums[i]
        if threshold == size:
            return num_max
        max_value = min(num_max, sum // (threshold - size) + 1)
        min_value = sum // threshold
        while True:
            mid_value = (max_value + min_value) // 2
            if mid_value == min_value:
                break
            division = 0
            for num in nums:
                division += num // mid_value
            if division <= threshold - size:
                max_value = mid_value
            else:
                min_value = mid_value
        return max_value


print(Solution().smallestDivisor([1,2,5,9], 6)) # 5
print(Solution().smallestDivisor([2,3,5,7,11], 11)) # 3
print(Solution().smallestDivisor([2,3,5,7,11], 5)) # 11
print(Solution().smallestDivisor([19], 5)) # 4


# Given an array of integers nums and an integer threshold, we will choose a positive integer divisor and divide all the array by it and sum the result of the division. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

# Each result of division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

# It is guaranteed that there will be an answer.

#  

# Example 1:

# Input: nums = [1,2,5,9], threshold = 6
# Output: 5
# Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
# If the divisor is 4 we can get a sum to 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2). 
# Example 2:

# Input: nums = [2,3,5,7,11], threshold = 11
# Output: 3
# Example 3:

# Input: nums = [19], threshold = 5
# Output: 4
#  

# Constraints:

# 1 <= nums.length <= 5 * 10^4
# 1 <= nums[i] <= 10^6
# nums.length <= threshold <= 10^6

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-the-smallest-divisor-given-a-threshold
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
