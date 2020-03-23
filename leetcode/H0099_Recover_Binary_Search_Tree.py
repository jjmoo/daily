from utils import TreeNode

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack, w1, w2, last = [], None, None, None
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack: break
            root = stack.pop()
            if last and root.val < last.val:
                if not w1: w1, w2 = last, root
                else: w2 = root
            last = root
            root = root.right
        w1.val, w2.val = w2.val, w1.val

    def recoverTreeYield(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def travel(node = root):
            stack = []
            while node or stack:
                while node:
                    stack.append(node)
                    node = node.left
                node = stack.pop()
                yield node
                node = node.right
        w1, w2, last = None, None, None
        for node in travel():
            if last and node.val < last.val:
                if not w1: w1, w2 = last, node
                else: w2 = node
            last = node
        w1.val, w2.val = w2.val, w1.val

    def recoverTreeMorris(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def travel(node = root):
            while node:
                if not node.left: 
                    yield node
                    node = node.right
                else:
                    prev = node.left
                    while prev.right and prev.right != node:
                        prev = prev.right
                    if not prev.right:
                        prev.right = node
                        node = node.left
                    else:
                        prev.right = None
                        yield node
                        node = node.right
        w1, w2, last = None, None, None
        for node in travel():
            if last and node.val < last.val:
                if not w1: w1, w2 = last, node
                else: w2 = node
            last = node
        w1.val, w2.val = w2.val, w1.val


test = Solution().recoverTreeMorris
root = TreeNode.create_tree([1,3,None,None,2])
test(root)
print(root)
root = TreeNode.create_tree([3,1,4,None,None,2])
test(root)
print(root)
root = TreeNode.create_tree([5,3,9,-2147483648,2])
test(root)
print(root)


# Two elements of a binary search tree (BST) are swapped by mistake.

# Recover the tree without changing its structure.

# Example 1:

# Input: [1,3,null,null,2]

#    1
#   /
#  3
#   \
#    2

# Output: [3,1,null,null,2]

#    3
#   /
#  1
#   \
#    2
# Example 2:

# Input: [3,1,4,null,null,2]

#   3
#  / \
# 1   4
#    /
#   2

# Output: [2,1,4,null,null,3]

#   2
#  / \
# 1   4
#    /
#   3
# Follow up:

# A solution using O(n) space is pretty straight forward.
# Could you devise a constant space solution?

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/recover-binary-search-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
