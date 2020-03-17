from utils import ListNode

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head: return None
        p, pp, cnt = head, head, 0
        while p.next and pp.next and pp.next.next:
            p, pp, cnt = p.next, pp.next.next, cnt + 1
            if p == pp: break
        else: return None
        c, pp = 1, p.next
        while p != pp:
            c, p, pp = c + 1, p.next, pp.next.next
        for _ in range(cnt - c): head = head.next
        while True:
            for _ in range(c):
                if p == head: return head
                p = p.next
            head = head.next

    def detectCycleFloyd(self, head: ListNode) -> ListNode:
        if not head: return None
        p, pp, cnt = head, head, 0
        while p.next and pp.next and pp.next.next:
            p, pp, cnt = p.next, pp.next.next, cnt + 1
            if p == pp: break
        else: return None
        while head != p:
            head, p = head.next, p.next
        return head


test = Solution().detectCycleFloyd
print(test(ListNode.create_cycle([3,2,0,-4,5,6,7,8,9,10,11,12,13,14,15], 11)).val)
print(test(ListNode.create_cycle([1,2], 0)).val)
print(test(ListNode.create_cycle([1], 0)).val)
print(test(ListNode.create_cycle([1], -1)))
print(test(ListNode.create_cycle([1], 0)).val)


# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

# Note: Do not modify the linked list.

#  

# Example 1:

# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.


# Example 2:

# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the first node.


# Example 3:

# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.


#  

# Follow-up:
# Can you solve it without using extra space?

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/linked-list-cycle-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
