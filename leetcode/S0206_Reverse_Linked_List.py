from utils import ListNode

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        r, p = None, head
        while p: p.next, r, p = r, p, p.next
        return r


test = Solution().reverseList
print(test(ListNode.create_list([1,2,3,4,5])))


# Reverse a singly linked list.

# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:

# A linked list can be reversed either iteratively or recursively. Could you implement both?
