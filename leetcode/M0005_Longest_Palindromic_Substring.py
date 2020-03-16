class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        n, length, start, end = len(s), 0, 0, 0
        memo = {}
        for j in range(n):
            for i in range(j, -1, -1):
                memo[i, j] = i == j or \
                    s[i] == s[j] and (i + 1 == j or memo[i + 1, j - 1])
                if memo[i, j] and j - i >= length:
                    start, end = i, j
                    length = end - start + 1
        return s[start : end + 1]
    
    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        memo, n, g_length, g_start, g_end = [(0, 0)], len(s), 0, 0, 0
        for i in range(1, n):
            if s[i - 1] == s[i]:
                memo.append((i - 1, i))
                if g_length < 2: g_length, g_start, g_end = 2, i - 1, i
            memo.append((i, i))
            if g_length < 1: g_length, g_start, g_end = 1, i, i
        tail = len(memo)
        while tail > 0:
            head = 0
            for i in range(tail):
                start, end = memo[i]
                if start > 0 and end < n - 1 and s[start - 1] == s[end + 1]:
                    start, end = start - 1, end + 1
                    memo[head] = start, end
                    head += 1
                    length = end - start + 1
                    if g_length < length: 
                        g_length, g_start, g_end = length, start, end
            tail = head
        return s[g_start : g_end + 1]
    
    def longestPalindrome3(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        n, cur = len(s), [0, 0, 0] # [length, start, end]
        def find(i, j):
            while i > 0 and j < n - 1 and s[i - 1] == s[j + 1]:
                i, j = i - 1, j + 1
            l = j - i + 1
            if l > cur[0]:
                cur[0] = l
                cur[1], cur[2] = i, j
        for i in range(1, n):
            if s[i - 1] == s[i]:
                find(i - 1, i)
            find(i ,i)
        return s[cur[1] : cur[2] + 1]

    def longestPalindromeManacher(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        t = '^#'
        for ch in s:
            t += ch + '#'
        t += '$'
        n = len(t)
        p, di, mx, center, length = [0] * n, 0, -1, 0, 0
        for i in range(n - 1):
            p[i] = min(p[(di << 1) - i], mx - i) if mx > i else 1
            while t[i + p[i]] == t[i - p[i]]: p[i] += 1
            if mx < i + p[i]: di, mx = i, i + p[i]
            if p[i] > length: center, length = i, p[i]
        start = (center - length) >> 1
        return s[start : start + length - 1]


test = Solution().longestPalindromeManacher
print('bab', test('babad'))
print('bb', test('cbbd'))
print('acbbca', test('ddacbbcaacbd'))


# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-palindromic-substring
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
