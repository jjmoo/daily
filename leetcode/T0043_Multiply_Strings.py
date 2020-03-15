class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if not num1 or not num2 or num1[0] == '0' or num2[0] == '0': return '0'
        nums = [[], []]
        for i, num in enumerate([num1, num2]):
            while True:
                num, sub = num[:-4], num[-4:]
                nums[i].append(int(sub))
                if not num: break
        n1, n2 = len(nums[0]), len(nums[1])
        result, product = '', [0] * (n1 + n2)
        for i in range(n1):
            for j in range(n2):
                product[i + j] += nums[0][i] * nums[1][j]
        for i in range(1, n1 + n2):
            product[i] += product[i - 1] // 10000
            product[i - 1] = product[i - 1] % 10000
        for i in range(n1 + n2 - 1, -1, -1):
            if not result or '0' == result: result = str(product[i])
            else: result += '%04d' % product[i]
        return result
    
    def multiplyDirectly(self, num1: str, num2: str) -> str:
        if not num1 or not num2 or num1[0] == '0' or num2[0] == '0': return '0'
        n1, n2 = len(num1), len(num2); n = n1 + n2
        result, product = '', [0] * n
        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                product[n - 2 - i - j] += int(num1[i]) * int(num2[j])
        for i in range(1, n):
            product[i] += product[i - 1] // 10
            product[i - 1] = product[i - 1] % 10
        for i in range(n - 1, -1, -1):
            if not result or '0' == result: result = str(product[i])
            else: result += str(product[i])
        return result


test = Solution().multiplyDirectly
print(6, test('2', '3'))
print(56088, test('123', '456'))
print(2895899850190521, test('123456789', '23456789'))
print(0, test('0', '45678'))


# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:

# Input: num1 = "123", num2 = "456"
# Output: "56088"
# Note:

# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0 itself.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/multiply-strings
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
