from utils import TreeNode

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def maxPath(node = root):
            if not node: return -99999999, -99999999
            left, right = maxPath(node.left), maxPath(node.right)
            max_end = max(node.val, left[0] + node.val, right[0] + node.val)
            max_below = max(max_end, left[1], right[1], node.val + left[0] + right[0])
            return max_end, max_below
        return maxPath()[1]


test = Solution().maxPathSum
print(test(TreeNode.create_tree([1,2,3])))
print(test(TreeNode.create_tree([-3])))
print(test(TreeNode.create_tree([-10,9,20,None,None,15,7])))
print(test(TreeNode.create_tree([-6,None,3,None,None,2])))


# Given a non-empty binary tree, find the maximum path sum.

# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

# Example 1:

# Input: [1,2,3]

#        1
#       / \
#      2   3

# Output: 6
# Example 2:

# Input: [-10,9,20,null,null,15,7]

#    -10
#    / \
#   9  20
#     /  \
#    15   7

# Output: 42

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/binary-tree-maximum-path-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
