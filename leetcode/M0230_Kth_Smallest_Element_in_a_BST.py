from typing import List
from utils import TreeNode

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def midOrder(node: TreeNode = root) -> List:
            if not node: return []
            return midOrder(node.left) + [node.val] + midOrder(node.right) 
        return midOrder()[k - 1]

    def kthSmallestLoop(self, root: TreeNode, k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right


test = Solution().kthSmallestLoop
print(1, test(TreeNode.create_tree([3,1,4,None,2]), 1))
print(3, test(TreeNode.create_tree([5,3,6,2,4,None,None,1]), 3))


# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

# Example 1:

# Input: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1
# Example 2:

# Input: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
