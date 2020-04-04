class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s
        if not s: return '*' == p[0] and self.isMatch(s, p[1:])
        if '*' == p[0]: return self.isMatch(s, p[1:]) or self.isMatch(s[1:], p)
        return p[0] in [s[0], '?'] and self.isMatch(s[1:], p[1:])

    def isMatchMemo(self, s: str, p: str) -> bool:
        def match(i = 0, j = 0):
            if memo[i][j] is None:
                if j == n: memo[i][j] = i == m
                elif i == m: memo[i][j] = '*' == p[j] and match(i, j + 1)
                elif '*' == p[j]: memo[i][j] = match(i, j + 1) or match(i + 1, j)
                else: memo[i][j] = p[j] in [s[i], '?'] and match(i + 1, j + 1)
            return memo[i][j]
        m, n = 0 if not s else len(s), 0 if not p else len(p)
        memo = [[None] * (n + 1) for _ in range(m + 1)]
        memo[m][n] = True
        return match()

    def isMatchDp(self, s: str, p: str) -> bool:
        m, n = 0 if not s else len(s), 0 if not p else len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = True
        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m: dp[i][j] = dp[i][j + 1] and '*' == p[j]
                elif '*' == p[j]: dp[i][j] = dp[i][j + 1] or dp[i + 1][j]
                else: dp[i][j] = p[j] in [s[i], '?'] and dp[i + 1][j + 1]
        return dp[0][0]


test = Solution().isMatchDp
print(False, test('aa', 'a'))
print(True, test('aa', '*'))
print(False, test('cb', '?a'))
print(True, test('adceb', '*a*b'))
print(False, test('acdcb', 'a*c?b'))
print(False, test('aaabbbaabaaaaababaabaaabbabbbbbbbbaabababbabbbaaaaba', 'a*******b'))


# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).

# Note:

# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like ? or *.
# Example 1:

# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input:
# s = "aa"
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# Example 3:

# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
# Example 4:

# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
# Example 5:

# Input:
# s = "acdcb"
# p = "a*c?b"
# Output: false

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/wildcard-matching
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
