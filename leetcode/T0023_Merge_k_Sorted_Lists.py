# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def to_string(node):
    if not node:
        return None
    sb = str(node.val)
    while node.next is not None:
        node = node.next
        sb += f'->{node.val}'
    return sb

def create_node_list(lists):
    node = dummy = ListNode(0)
    for val in lists:
        node.next = ListNode(val)
        node = node.next
    print('create:', to_string(dummy.next))
    return dummy.next

def create_lists(lists):
    return [create_node_list(l) for l in lists]


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        i, n = 0, len(lists)
        while i < n:
            if not lists[n - 1]: n -= 1; continue
            if lists[i]: i += 1; continue
            else: lists[i] = lists[n - 1]; lists[n - 1] = None
        if n <= 0:
            return None
        def build(index):
            while index <= n // 2 - 1:
                left = (index << 1) + 1
                right = (index << 1) + 2
                less = right if right < n and \
                    lists[right].val < lists[left].val else left
                if lists[index].val > lists[less].val:
                    tmp = lists[index]
                    lists[index] = lists[less]
                    lists[less] = tmp
                    index = less
                else:
                    break
        for i in range(n // 2 - 1, -1, -1): build(i)
        p = dummy = ListNode(0)
        while n:
            p.next = lists[0]
            p = p.next
            if p.next:
                lists[0] = p.next
            else:
                lists[0] = lists[n - 1]
                n = n - 1
            if n > 1:
                build(0)
        return dummy.next


    def mergeKListsHeapq(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        import heapq
        heap = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i))
                lists[i] = l.next
        p = dummy = ListNode(0)
        while heap:
            val, index = heap[0]
            p.next = ListNode(val)
            p = p.next
            if lists[index]:
                heapq.heapreplace(heap, (lists[index].val, index))
                lists[index] = lists[index].next
            else:
                heapq.heappop(heap)
        return dummy.next


test = Solution().mergeKListsHeapq
print(to_string(test(create_lists([[1,4,5], [1,3,4], [2,6]]))))
print(to_string(test(create_lists([]))))
print(to_string(test(create_lists([[]]))))
print(to_string(test(create_lists([[1]]))))
print(to_string(test(create_lists([[0,2,5]]))))
print(to_string(test(create_lists([[-10,-9,-9,-3,-1,-1,0],[-5],[4],[-8],[],[-9,-6,-5,-4,-2,2,3],[-3,-3,-2,-1,0]]))))
print(to_string(test(create_lists([[-8,-7,-6,-3,-2,-2,0,3],[-10,-6,-4,-4,-4,-2,-1,4],[-10,-9,-8,-8,-6],[-10,0,4]]))))


# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Example:

# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/merge-k-sorted-lists
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
