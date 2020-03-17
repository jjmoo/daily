import time

class Benchmark():
    """Benchmark programs."""
    def __init__(self, prefix=None):
        self.prefix = prefix + ' ' if prefix else ''

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, *args):
        print('%stime: %.4f sec' % (self.prefix, time.time() - self.start))


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        sb = str(self.val)
        p = self.next
        while p:
            sb += f'->{p.val}'
            p = p.next
        return sb

    @staticmethod
    def create_list(l):
        p = dummy = ListNode(0)
        for x in l:
            p.next = ListNode(x)
            p = p.next
        print('create:', dummy.next)
        return dummy.next

    @staticmethod
    def create_cycle(l, pos):
        p = head = ListNode.create_list(l)
        if pos >= 0:
            for _ in range(pos): p = p.next
            tail = p
            while tail.next: tail = tail.next
            tail.next = p
        return head

    @staticmethod
    def create_lists(lists):
        return [ListNode.create_list(l) for l in lists]


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __str__(self):
        h = self.__height()
        i, l = 0, [None] * (2 ** h - 1)
        l[0], result, nl = self, '\n', 0
        for i, n in enumerate(l):
            if n:
                if n.left: l[2 * i + 1] = n.left
                if n.right: l[2 * i + 2] = n.right
                result += ' %3d' % n.val
            else:
                result += '   x'
            if nl == i:
                nl, result = nl * 2 + 2, result + '\n'
        return result

    def __height(self):
        return 1 + max(self.left.__height() if self.left else 0, \
            self.right.__height() if self.right else 0)

    @staticmethod
    def create_tree(l):
        n, result = len(l), [None if x == None else TreeNode(x) for x in l]
        for i, node in enumerate(result):
            if not node: continue
            if 2 * i + 1 < n: node.left = result[2 * i + 1]
            if 2 * i + 2 < n: node.right = result[2 * i + 2]
        print('create:', result[0])
        return result[0]
