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
