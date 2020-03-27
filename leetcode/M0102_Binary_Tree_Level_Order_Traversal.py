from typing import List
from utils import TreeNode
from collections import deque

def travel_level(node):
    queue = deque()
    queue.append((1, node))
    cur_level, nodes = 1, []
    while queue:
        level, node = queue.popleft()
        if level > cur_level:
            yield cur_level, list(nodes)
            cur_level = level
            nodes.clear()
        nodes.append(node)
        if node.left: queue.append((level + 1, node.left))
        if node.right: queue.append((level + 1, node.right))
    yield cur_level, nodes

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return [[]]
        return [[node.val for node in nodes] for _, nodes in travel_level(root)]


test = Solution().levelOrder
print(test(TreeNode.create_tree([3,9,20,None,None,15,7])))
print(test(TreeNode.create_tree([3])))
print(test(None))


# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
