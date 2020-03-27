from utils import TreeNode
from typing import List
from M0102_Binary_Tree_Level_Order_Traversal import travel_level

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        for level, nodes in travel_level(root):
            for node in nodes:
                if not node.left and not node.right:
                    return level


test = Solution().minDepth
print(test(TreeNode.create_tree([3,9,20,None,None,15,7])))


# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Example:

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its minimum depth = 2.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/minimum-depth-of-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
