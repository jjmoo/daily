from utils import ListNode

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = dummy = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        p.next = l1 if l1 else l2
        return dummy.next


test = Solution().mergeTwoLists
print('1->1->2->3->4->4', test(ListNode.create_node([1,2,4]), ListNode.create_node([1,3,4])))
print('1', test(ListNode.create_node([]), ListNode.create_node([1])))
print('', test(ListNode.create_node([]), ListNode.create_node([])))


# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
