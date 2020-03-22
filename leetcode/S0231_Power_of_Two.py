class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (-n) == n

    def isPowerOfTwo2(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0


test = Solution().isPowerOfTwo
print(True, test(1))
print(True, test(16))
print(False, test(218))


# Given an integer, write a function to determine if it is a power of two.

# Example 1:

# Input: 1
# Output: true 
# Explanation: 2^0 = 1
# Example 2:

# Input: 16
# Output: true
# Explanation: 2^4 = 16
# Example 3:

# Input: 218
# Output: false