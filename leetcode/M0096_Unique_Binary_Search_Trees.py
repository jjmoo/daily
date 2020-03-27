from utils import Benchmark

class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1: return 1
        memo = [1] * (n + 1)
        for i in range(2, n + 1):
            cnt = 0
            for j in range(i):
                cnt += memo[j] * memo[i - 1 - j]
            memo[i] = cnt
        return memo[n]


with Benchmark('test'):
    test = Solution().numTrees
    print(5, test(3))
    print(5, test(10))


# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

# Example:

# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/unique-binary-search-trees
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
