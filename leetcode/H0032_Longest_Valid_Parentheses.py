from utils import Benchmark

class Solution:
    def longestValidParenthesesTimeout(self, s: str) -> int:
        if not s: return 0
        def valid(start, end):
            if start >= end: return True
            cnt = 0
            for i in range(start, end):
                if '(' == s[i]: cnt += 1
                elif 0 == cnt: return False
                else: cnt -= 1 
            return 0 == cnt
        n, max_l = len(s), 0
        for i in range(n):
            for j in range(n, i, -1):
                if valid(i, j):
                    max_l = max(max_l, j - i)
                    break
        return max_l

    def longestValidParenthesesMy(self, s: str) -> int:
        if not s: return 0
        stack, l, max_l = [], 0, 0
        for ch in s:
            if '(' == ch:
                stack.append(l)
                l = 0
            elif stack:
                l += 2 + stack.pop()
                max_l = max(max_l, l)
            else:
                l = 0
        return max_l

    def longestValidParenthesesDp(self, s: str) -> int:
        if not s: return 0
        n = len(s)
        dp = [0] * n
        for i in range(1, n):
            if '(' == s[i]: continue
            if '(' == s[i - 1]:
                dp[i] = 2 + (0 if i < 2 else dp[i - 2])
            else:
                pair = i - 1 - dp[i - 1]
                if pair >= 0 and '(' == s[pair]:
                    dp[i] = 2 + dp[i - 1] + (dp[pair - 1] if pair > 0 else 0)
        return max(dp)

    def longestValidParenthesesStack(self, s: str) -> int:
        if not s: return 0
        stack, max_l = [-1], 0
        for i, ch in enumerate(s):
            if '(' == ch:
                stack.append(i)
            else:
                stack.pop()
                if not stack: stack.append(i)
                else: max_l = max(max_l, i - stack[-1])
        return max_l

    def longestValidParenthesesTwo(self, s: str) -> int:
        if not s: return 0
        max_l = 0
        left, right = 0, 0
        for ch in s:
            if '(' == ch: left += 1
            else: right += 1
            if left == right: max_l = max(max_l, left + right)
            elif left < right: left, right = 0, 0
        left, right = 0, 0
        for ch in reversed(s):
            if '(' == ch: left += 1
            else: right += 1
            if left == right: max_l = max(max_l, left + right)
            elif left > right: left, right = 0, 0
        return max_l


with Benchmark('test'):
    test = Solution().longestValidParenthesesTwo
    print(2, test('()'))
    print(4, test(')()())'))
    print(2, test('()(()'))
    print(6, test('))())(()))()(((()())(('))
    print(8, test('(((()))()'))
    print(490, test('))())(()))()(((()())(()(((()))))((()(())()((((()))())))())))()(()(()))))())(((())(()()))((())()())((()))(()(())(())((())((((()())()))((()(())()))()(()))))))()))(()))))()())()())()()()()()()()))()(((()()((()(())((()())))(()())))))))(()()(())())(()))))))()()())((((()()()())))))((())(())()()(()((()()))()()())(()())()))()(()(()())))))())()(())(()))(())()(())()((())()((((()()))())(((((())))())())(()((())((()()((((((())))(((())))))))(()()((((((()(((())()(()))(()())((()(((()((()(())())()())(((()))()(((()))))(())))(())()())()(((()))))((())())))())()()))((((()))(())()())()(((())(())(()()((())()())()()())())))((()())(()((()()()(()())(()))(()())((((()(()(((()(((())()((()(()))())()())))))))))))()())()(()(((())()))(((()))((((()())())(()())((()())(()()((()((((()())))()(())(())()))))(())())))))(((((((())(((((()))()))(()()()()))))))(()(()(()(()()(((()()))((()))())((())())()())()))()()(((())))()(())()()(())))(((()))))))))(())((()((()((()))))()()()((())((((((((((()(())))(())((()(()())())(((((((()()()()))())(((()())()(()()))))(()()))))(((()()((()()()(((()))))(()()())()()()(()))))()(())))))))()((((((((()((())))))))(()))()((()())())('))


# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

# Example 1:

# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# Example 2:

# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-valid-parentheses
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
