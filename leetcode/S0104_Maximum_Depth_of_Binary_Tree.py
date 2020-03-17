from utils import TreeNode

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return 0 if not root else 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


test = Solution().maxDepth
print(test(TreeNode.create_tree([3,9,20,None,None,15,7])))
print(test(TreeNode.create_tree([3,9,20,None,None,15])))
print(test(TreeNode.create_tree([3,9,20,None,None,15,7,None,None,None,None,8])))


# Given a binary tree, find its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Note: A leaf is a node with no children.

# Example:

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-depth-of-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
