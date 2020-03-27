from utils import TreeNode

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def check(node, start, end):
            if not node: return True
            if node.val <= start or node.val >= end: return False
            return check(node.left, start, node.val) and check(node.right, node.val, end)
        return check(root, float('-inf'), float('inf'))


test = Solution().isValidBST
print(True, test(TreeNode.create_tree([2,1,3])))
print(False, test(TreeNode.create_tree([5,1,4,None,None,3,6])))


# Given a binary tree, determine if it is a valid binary search tree (BST).

# Assume a BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Example 1:

#     2
#    / \
#   1   3

# Input: [2,1,3]
# Output: true
# Example 2:

#     5
#    / \
#   1   4
#      / \
#     3   6

# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/validate-binary-search-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
