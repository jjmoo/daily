from utils import TreeNode
from typing import List
from M0102_Binary_Tree_Level_Order_Traversal import travel_level

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        return [[node.val for node in (nodes if level % 2 else reversed(nodes))] for level, nodes in travel_level(root)]


test = Solution().zigzagLevelOrder
print(test(TreeNode.create_tree([3,9,20,None,None,15,7])))
print(test(TreeNode.create_tree([3])))
print(test(None))


# Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

# For example:
# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:

# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
