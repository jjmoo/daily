from utils import ListNode

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return l1 if not l2 else l2
        p = dummy = ListNode(0)
        while l1 or l2 or dummy.val:
            p.next = ListNode(dummy.val)
            p = p.next
            if l1:
                p.val += l1.val
                l1 = l1.next
            if l2:
                p.val += l2.val
                l2 = l2.next
            dummy.val = p.val // 10
            p.val = p.val - dummy.val * 10
        return dummy.next


test = Solution().addTwoNumbers
print(807, test(ListNode.create_node([2,4,3]), ListNode.create_node([5,6,4])))
print(468, test(ListNode.create_node([3]), ListNode.create_node([5,6,4])))
print(465, test(ListNode.create_node([]), ListNode.create_node([5,6,4])))
print(1000, test(ListNode.create_node([1]), ListNode.create_node([9,9,9])))


# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/add-two-numbers
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
