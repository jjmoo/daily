from typing import List
from utils import TreeNode

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n <= 0: return []
        memo = [[[] for _ in range(n + 2)] for _ in range(n + 2)]
        for i in range(0, n + 2):
            memo[i][i].append(None)
        for j in range(1, n + 1):
            for i in range(1, n + 2 - j):
                for k in range(i, i + j):
                    for left in memo[i][k]:
                        for right in memo[k + 1][i + j]:
                            node = TreeNode(k)
                            node.left = left
                            node.right = right
                            memo[i][i + j].append(node)
        return memo[1][1 + n]


test = Solution().generateTrees
for tree in test(3): print(tree)


# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

# Example:

# Input: 3
# Output:
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/unique-binary-search-trees-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
