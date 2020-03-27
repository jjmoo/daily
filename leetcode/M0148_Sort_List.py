from utils import ListNode

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head: return None
        def cut(start, length):
            for _ in range(length - 1):
                if not start.next: return None
                start = start.next
            start.next, start = None, start.next
            return start
        def prepare(start, length):
            first, second = start, cut(start, length)
            rest = cut(second, length) if second else None
            return first, second, rest
        def merge(head, first, second):
            while first or second:
                if not second or first and first.val < second.val:
                    head.next, first = first, first.next
                else: head.next, second = second, second.next
                head = head.next
            return head
        dummy = ListNode(0)
        step, dummy.next = 1, head
        while True:
            rest, head = dummy.next, dummy
            while rest:
                first, second, rest = prepare(rest, step)
                if not second and first is dummy.next: return dummy.next
                head = merge(head, first, second)
            step <<= 1


test = Solution().sortList
print(test(ListNode.create_list([4,2,1,3])))
print(test(ListNode.create_list([-1,5,3,4,0])))
print(test(ListNode.create_list([-1])))


# Sort a linked list in O(n log n) time using constant space complexity.

# Example 1:

# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:

# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
