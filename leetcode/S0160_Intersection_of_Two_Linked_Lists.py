from utils import ListNode

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB: return None
        def get_len(head):
            p, l = head, 1
            while p.next: p, l = p.next, l + 1
            return l
        la, lb = get_len(headA), get_len(headB)
        head1, head2 = (headA, headB) if la > lb else (headB, headA)
        for _ in range(abs(la - lb)): head1 = head1.next
        while head1 != head2:
            if head1.next and head2.next:
                head1, head2 = head1.next, head2.next
            else: return None
        return head1

    def getIntersectionCat(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB: return None
        p1, p2, switch = headA, headB, False
        while p1 != p2:
            p1 = p1.next if p1.next else headB
            if p2.next: p2 = p2.next
            elif not switch: p2, switch = headA, True
            else: return None
        return p1


test = Solution().getIntersectionCat
la = ListNode.create_list([4,1])
lb = ListNode.create_list([5,0,1])
lc = ListNode.create_list([8,4,5])
print(test(la, lb))
print(test(la + lc, lb + lc))


# Write a program to find the node at which the intersection of two singly linked lists begins.
# For example, the following two linked lists:
# begin to intersect at node c1.

# Example 1:
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
# Output: Reference of the node with value = 8
# Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

# Example 2:
# Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
# Output: Reference of the node with value = 2
# Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
 

# Example 3:
# Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# Output: null
# Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
# Explanation: The two lists do not intersect, so return null.

# Notes:
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.
