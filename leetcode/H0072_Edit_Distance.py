class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 or not word2:
            if not word1 and not word2: return 0
            else: return len(word1) if word1 else len(word2)
        n1, n2 = len(word1), len(word2)
        memo = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(n1): memo[i][-1] = i + 1
        for j in range(n2): memo[-1][j] = j + 1
        for i in range(n1):
            for j in range(n2):
                if word1[i] == word2[j]:
                    memo[i][j] = memo[i - 1][j - 1]
                else:
                    memo[i][j] = 1 + min(memo[i - 1][j - 1], memo[i][j - 1], memo[i - 1][j])
        return memo[n1 - 1][n2 - 1]


test = Solution().minDistance
print(3, test('horse', 'ros'))
print(5, test('intention', 'execution'))


# Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

# You have the following 3 operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character
# Example 1:

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
# Example 2:

# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/edit-distance
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
