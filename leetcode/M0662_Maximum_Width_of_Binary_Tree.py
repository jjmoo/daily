from utils import TreeNode

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        from collections import deque
        queue, cur_level, max_width = deque(), 0, 0
        start_index, last_index = 0, 0
        queue.append((1, 0, root))
        while queue:
            level, index, node = queue.popleft()
            if level > cur_level:
                cur_level = level
                max_width = max(max_width, last_index - start_index + 1)
                start_index = index
            last_index = index
            if node.left:
                queue.append((level + 1, index * 2 + 1, node.left))
            if node.right:
                queue.append((level + 1, index * 2 + 2, node.right))
        max_width = max(max_width, last_index - start_index + 1)
        return max_width


test = Solution().widthOfBinaryTree
print(4, test(TreeNode.create_tree([1,3,2,5,3,None,9])))
print(2, test(TreeNode.create_tree([1,3,None,5,3])))
print(2, test(TreeNode.create_tree([1,3,2,5])))
print(8, test(TreeNode.create_tree([1,3,2,5,None,None,9,6,None,None,None,None,None,None,7])))


# Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

# The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

# Example 1:

# Input: 

#            1
#          /   \
#         3     2
#        / \     \  
#       5   3     9 

# Output: 4
# Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
# Example 2:

# Input: 

#           1
#          /  
#         3    
#        / \       
#       5   3     

# Output: 2
# Explanation: The maximum width existing in the third level with the length 2 (5,3).
# Example 3:

# Input: 

#           1
#          / \
#         3   2 
#        /        
#       5      

# Output: 2
# Explanation: The maximum width existing in the second level with the length 2 (3,2).
# Example 4:

# Input: 

#           1
#          / \
#         3   2
#        /     \  
#       5       9 
#      /         \
#     6           7
# Output: 8
# Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).


# Note: Answer will in the range of 32-bit signed integer.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-width-of-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
