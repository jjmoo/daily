class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s is None or p is None:
            return s == p
        return self.__isMatch(s, 0, len(s), p, 0, len(p))

    def __isMatch(self, s, si, sl, p, pi, pl):
        # print('to match:', s[si:], p[pi:])
        while True:
            if pi + 1 < pl and p[pi + 1] == '*':
                if self.__isMatch(s, si, sl, p, pi + 2, pl):
                    return True
                for i in range(si, sl):
                    if p[pi] == '.' or p[pi] == s[i]:
                        if self.__isMatch(s, i + 1, sl, p, pi + 2, pl):
                            return True
                    else:
                        si, pi = i, pi + 2
                        break
                else:
                    return False
            if pi < pl and si < sl:
                if p[pi] == '.' or p[pi] == s[si]:
                    pi, si = pi + 1, si + 1
                    continue
                else:
                    return False
            else:
                return si >= sl and pi >= pl

    def isMatchRec(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s
        match_head = bool(s) and (s[0] == p[0] or p[0] == '.')
        if len(p) >= 2 and p[1] == '*':
            return self.isMatchRec(s, p[2:]) or \
                match_head and self.isMatchRec(s[1:], p)
        else:
            return match_head and self.isMatchRec(s[1:], p[1:])

    def isMatchUpDown(self, s, p):
        memo = {}
        ls, lp = len(s), len(p)
        def dp(i, j):
            if (i, j) not in memo:
                if j >= lp:
                    memo[i, j] = bool(i >= ls)
                else:
                    match_head = i < ls and (s[i] == p[j] or p[j] == '.')
                    if j + 1 < lp and p[j + 1] == '*':
                        memo[i, j] = dp(i, j + 2) or (match_head and dp(i + 1, j))
                    else:
                        memo[i, j] = match_head and dp(i + 1, j + 1)
            return memo[i, j]
        return dp(0, 0)

    def isMatchDownUp(self, s, p):
        ls, lp = len(s), len(p)
        dp = [[False] * (lp + 1) for _ in range(ls + 1)]
        dp[-1][-1] = True
        for i in range(ls, -1, -1):
            for j in range(lp - 1, -1, -1):
                match_head = i < ls and (s[i] == p[j] or p[j] == '.')
                if j + 1 < lp and p[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] or (match_head and dp[i + 1][j])
                else:
                    dp[i][j] = match_head and dp[i + 1][j + 1]
        return dp[0][0]


test = Solution().isMatchDownUp
print(False, test("ab", ".*c"))
print(True, test("aa", ".a"))
print(False, test("aa", "a"))
print(True, test("aa", "a*"))
print(True, test("ab", ".*"))
print(True, test("aab", "c*a*b"))
print(False, test("mississippi", "mis*is*p*."))


# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# Note:

# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like . or *.
# Example 1:

# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:

# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:

# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# Example 4:

# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
# Example 5:

# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/regular-expression-matching
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
