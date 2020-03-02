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
